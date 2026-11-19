# But what is a neural network? (3blue1brown, aircAruvnKk)

## Structure arc
Hook (0:04-1:15): a sloppy 28x28 "3" that your brain reads effortlessly, flipped into "now write a program for it" — trivial becomes daunting. Roadmap and caveats (1:15-2:39): structure only, plain vanilla, will fall short. Minimal vocabulary (2:39-5:36): neuron = number, layers, activation, a trained net lighting up. Motivation (5:36-8:23): why layers might work — digits into loops and lines, loops into edges, plus speech as a parallel. Mechanism by design (8:23-12:31): one edge-detecting neuron gets weights, a weighted sum, sigmoid, bias; then scale-up to ~13,000 knobs. Compaction (13:22-15:10): sigmoid(Wa+b). Redefinition and close (15:10-16:15): a neuron is a function; the net is a function. Expert coda with Lisha Li on ReLU.

## Strongest moves
1. **Hope-before-mechanism (5:36-7:51).** Before any math, it asks what the hidden layers would ideally do. The edge -> loop -> digit story turns the architecture into a plan, so the weights at 9:11 answer a question the viewer already has. It is openly flagged as a hope, to be checked after training (7:35).
2. **Design-it-yourself on one neuron (8:23-11:27).** "What dials and knobs should you be able to tweak?" Weights are drawn as a green/red pixel grid over the image. Zeroing everything except one region, then adding a negative surround, builds an edge detector you can see. Bias is motivated by "only active above 10".
3. **Tiny to huge (11:27-12:31).** One neuron, then 784x16, then 13,000 parameters. The jump in scale is what defines "learning": finding settings for all of them.
4. **Late, optional notation (13:22).** The matrix form comes in as what you would see "if you read up more". Its use is justified (compact, fast libraries), and it points out to the linear algebra series.
5. **Thin definition, upgraded (2:39 -> 15:10).** "A thing that holds a number" becomes "a function". Holding the simplification back until the end keeps early symbol cost low.

## What is unusual
Honest caveats run the whole video: the layer sizes are arbitrary and chosen to fit the screen (4:06), the hope may be false (7:35), and the guest later says sigmoid is outdated (16:48). The hand-setting thought experiment (12:47) is pitched as a way to get to know the weights, not as an algorithm. There is no inline quiz, and no insight is left for the learner to find. Everything is stated, though always as the answer to a question that came just before.

## Principle verdicts (brief)
Confirmed: 1 (familiar digit), 2 (symbols deferred), 4 (brain analogy toward weighted sums), 10 (neuron -> layer -> network), 11 (strict dependency order), 12 (speech, linear algebra series, guest), 13 (justifies sigmoid, bias, matrices). Partly: 3, 5, 6, 8, 9. Not observed: 7. On 8, notation shows up late (13:22) and the ideas come in steady beats of roughly 20-40 s, but the transcript gives no speech-rate evidence either way.

## Velocity implications
- The orchestrator should open a mechanism with "what would we hope each part does?" and take the learner's decomposition before showing weights.
- The scene builder should draw parameters in the input's own geometry (a weight grid over the pixels).
- The learner model should tag provisional definitions and schedule an upgrade beat.
- Voice should label hypotheses as hypotheses, then come back to them.
- An eval: notation must come after concrete use of its concept.
