# Embedded / IoT / device control

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The feature changes firmware, hardware interaction, sensor/control pipeline or constrained-device state.

Do not select merely because C/Rust exists without a device boundary; do not infer hardware from language.

## Decisions before sectioning

- Confirm actual board/RTOS/interface and what host simulation cannot prove.
- Name interrupt/task/buffer ownership, timing/units/calibration and watchdog/resource constraints that the change activates.
- Distinguish requested power-loss/reconnect/update behavior from speculative safety/certification promises.

## Handoff and smallest useful evidence

Use existing HAL/device fixtures and a controlled real-device check when essential; record physical/environment limits. Keep actuator changes within approved operating conditions.

## Scope boundary

No new RTOS, bootloader, certification regime, universal fault-tolerance or unsupported hardware matrix. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Zephyr interrupts](https://docs.zephyrproject.org/latest/kernel/services/interrupts.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
