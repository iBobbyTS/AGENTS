# Network Debugging

Load this playbook for DNS, routing, TCP, TLS, proxy/load-balancer, HTTP transport, browser CORS, intermittent connectivity, or service-to-service network failures.

## Walk the protocol ladder

Do not jump from “request failed” directly to application code. Localize in order:

```text
name resolution
→ route/address family
→ TCP connection
→ TLS handshake and identity
→ proxy/load balancer
→ HTTP request/response
→ browser policy such as CORS
→ application behavior
```

Capture evidence from the failing client environment and, when possible, the receiving side. A successful request from your laptop does not prove a container, CI runner, browser, or user network follows the same path.

## Failure contract

Record:

- source environment/process/container/browser;
- hostname, resolved IPs, IPv4/IPv6 choice, port, protocol and SNI;
- proxy/VPN/service-mesh/load-balancer path;
- exact method, URL, headers/body shape, status/error and timing;
- certificate chain/hostname/validity result;
- whether failure is connect, handshake, first byte, mid-transfer, reset, timeout, or browser policy;
- request ID, connection ID, timestamps, and server-side observation.

## Safe client-side probes

Adapt commands to the environment and redact output before persisting it.

```bash
# DNS
dig +short example.com A
dig +short example.com AAAA

# TCP reachability
nc -vz example.com 443

# TLS/SNI and certificate chain
openssl s_client -connect example.com:443 -servername example.com -showcerts </dev/null

# HTTP details
curl -v --connect-timeout 10 --max-time 30 https://example.com/path
curl --trace-time --trace-ascii trace.txt https://example.com/path
```

`curl -v` and traces can expose authorization headers, cookies, URLs, and payloads. Use redacted test credentials or sanitize artifacts.

Do not use `-k`/`--insecure` as a repair. It can be a narrowly controlled diagnostic comparison only when the security consequence is understood and the result is not persisted as production configuration.

## DNS and address family

Compare:

- resolver configuration and search domains;
- authoritative answer versus local/container/OS cache;
- split-horizon/VPN results;
- A and AAAA records and which address the client selected;
- TTL and deployment/failover timing;
- container or service-discovery DNS names versus host names.

If IPv4 succeeds and IPv6 fails, localize route/firewall/listener parity rather than forcing IPv4 without understanding the deployment contract.

## TCP, resets, and timeouts

Determine where the timeout occurs:

- DNS lookup;
- connection establishment;
- TLS handshake;
- waiting for response headers;
- response body transfer;
- idle pooled connection reuse;
- proxy or server request deadline.

Capture server accept/access logs and process state for the same timestamp. A client timeout does not establish whether the request reached or completed at the server.

Use packet capture only when higher-level evidence cannot distinguish the cause:

```bash
sudo tcpdump -i <interface> -nn host <ip> and port <port> -w capture.pcap
```

Packet capture may require privilege and can collect sensitive unrelated traffic. Narrow capture filters, duration, and storage; obtain authorization. Analyze with Wireshark display filters after capture.

## TLS

Inspect:

- SNI hostname and certificate SAN match;
- complete intermediate chain;
- validity times and system clock;
- trusted root store in the actual client/container;
- protocol/cipher compatibility;
- mutual TLS client certificate and key;
- proxy TLS termination and re-encryption;
- certificate deployment consistency across load-balancer nodes.

A browser, Node, Python, container, and system curl may use different trust stores or proxy settings. Test the actual runtime.

## Proxy, load balancer, and service mesh

Correlate:

```text
client request ID
→ edge access log
→ upstream selection
→ backend access log
→ response/termination reason
```

Check route rules, host header, path rewriting, health state, connection reuse, retry policy, body limits, idle/request timeouts, and deployment skew. Proxy retries can duplicate unsafe requests or hide one failing backend.

## HTTP and CORS

CORS is a browser access-control decision, not basic network reachability.

For browser failures inspect:

- whether a preflight `OPTIONS` request occurred;
- requested method and headers;
- `Origin` and response `Access-Control-*` headers;
- credentials mode and exact origin, including scheme/host/port;
- redirects during preflight or credentialed requests;
- cache/CDN variation on `Origin`.

Compare browser Network evidence with a direct client. A successful curl request can coexist with a browser CORS failure because curl does not enforce browser CORS policy.

## Containers and host boundaries

Load [docker-containers.md](docker-containers.md) when relevant. Verify:

- host port publication versus container listening address/port;
- `localhost` meaning inside each network namespace;
- Compose service-name DNS and network attachment;
- container resolver and proxy environment;
- health check path versus real request path;
- MTU/VPN issues on bridged/overlay networks.

## Common causal chains

```text
container trusts different CA store → TLS fails only in container
AAAA record selected → IPv6 route missing → intermittent client-family-dependent timeout
proxy request timeout → backend continues mutation → client retry duplicates work
stale pooled connection after load-balancer idle timeout → first reused request resets
missing Vary: Origin at cache → CORS headers for one origin served to another
service listens on 127.0.0.1 in container → health check inside container passes → published port cannot reach it
```

## Completion evidence

- first failing protocol boundary;
- client and server/proxy evidence correlated by time/ID;
- verification from the original environment and address family;
- TLS validation remains enabled;
- packet/trace artifacts redacted or removed after use.
