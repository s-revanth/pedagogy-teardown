# How PNG works (Reducible, 32 min)

## Arc
Hook is a promise: PNG is lossless and clever, but slow, and a 50x faster rival (QOI) arrives at the end. Then a tool stack: Huffman (2:04), run-length (4:24), LZSS (5:05), filtering (13:41), deflate recap (21:00), then QOI (23:17) as the simplicity counterweight, a moral, and a sponsor read.

## Strongest moves
1. **Each tool fails on a tiny input before the next arrives.** RLE breaks on a two-pixel pattern (4:37). The gradient image (13:13) defeats both Huffman and LZSS, and the video lingers in the despair ("so depressing") before offering filtering. The learner feels the need before seeing the fix.
2. **Reduce to a solved problem, said out loud (13:55).** The narrator names the two options, invent new or transform the input, so filtering is a lesson in strategy, not just a PNG detail.
3. **Hand execution of LZSS (6:44-9:30).** One short text, every step shown: literal, back reference, window slide. Decoding is shown too (9:03) so losslessness is verified, not asserted. The overlap case (offset 2, length 4, 10:39-12:18) is introduced as "may surprise you" and pays off as free run-length coding.
4. **Honest caveats as trust capital.** 1.89 bits is misleading because the tree must be stored (3:28); the min-sum filter heuristic has no proof (20:19); 5^240 shows why brute force is out (18:29).
5. **QOI as five byte-aligned rules (23:44).** A rule-list interface on a 64-pixel image; the result (50 of 192 bytes) is computed live, and the viewer is invited to implement it.

## Unusual
No analogy anywhere; the familiar anchor is a bag of pixels and the question "how few bits?". Delivery is a story arc across two formats rather than one algorithm. The end moral (simple beats clever) ties to a creator's story, which is rare in algorithm videos.

## Principles
Confirmed: 1, 5, 6, 9, 10, 11. Partly: 2, 4 (no analogy), 7 (presenter supplies the fix), 8 (flat speech; slowing comes from many small worked steps in LZSS), 12, 13. Not observed: 3.

## Velocity implications
- Add a "stack of tools" playbook: failure input scene, then fix, then recap diagram.
- Voice can say the choice aloud ("new approach or transform the problem") at decision points.
- Ghost hands should step the sliding window one char at a time with identical timing, so the pattern repeats visibly.
- Eval: caveats appear at least once per video where a number could mislead.
