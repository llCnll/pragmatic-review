Focus on mixed responsibilities, hidden dependencies, unclear facts or ownership, and structures that make the next relevant change difficult.

Trace a use case through its decision, state, and side-effect boundaries. For helpers, base classes, or Mixins, identify the actual collaborators and shared state; assess whether the split reduces total reasoning cost.

Use repository architecture as the baseline. Favor the smallest improvement that makes ownership, inputs, and control flow explicit. Evaluate file count and class choice through demonstrated reasoning or change cost.
