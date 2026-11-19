# Bitcoin: teardown

**Arc.** Hook and invent-it promise (0:03-1:46); friends' ledger (2:36); signatures (3:31); replay fix (6:40); balance rule and "ledger dollars" (7:16-9:49); replicated ledger puzzle (10:05); hash functions (12:22); proof of work (14:38); blocks, mining, longest chain (16:04-19:38); attacker walkthrough (19:38); real parameters (21:45).

**Strongest moves**
1. Patch chain (3:31, 6:40, 7:33, 10:22): each mechanism arrives as a repair. Forgery leads to signatures, replay leads to unique IDs, defaulting debtors lead to the balance rule, central website leads to replicated ledgers. No component is introduced before its need.
2. Puzzle posed to the viewer (11:15): "can you come up with a protocol" is voiced as a real challenge, with the solution teased at 11:32 but delayed for a hash-function detour. This is the video's tension peak.
3. Hash puzzle made tangible (14:38-15:47): 30 leading zeros gives roughly a billion guesses, with an instant check, so "proof of work" is felt as asymmetric cost.
4. Attacker walkthrough (19:38-21:29): Alice tries to feed Bob a fake fork. The need for near-majority compute and the "wait several blocks" advice follow from the simulation, not from assertion.
5. Honest caveats (13:48): hardness of reversing SHA256 is unproven, yet the web depends on it. Also permission to skip (1:46).

**Unusual.** Gold-mining analogies are explicitly rejected (1:28) in favor of describing what computers do. Toy numbers (60 zeros, 10 LD) are used until the end, when real ones (10 minutes, halving, 21M) are revealed (22:03).

**Principle verdicts.** 1, 2, 5, 6, 7, 11, 12, 13 confirmed; 3 not observed; 4 partly (analogy rejected); 8 partly (runway long, no rate data); 9, 10 partly.

**Velocity implications**
- Orchestrator: structure playbooks as failure chains.
- Scene builder: an adversary actor that attacks the current rules.
- Voice: pose the puzzle and wait.
- Learner model: store the failure each concept patched, and test with "what breaks without it".
- Evals: toy parameters before real ones.
