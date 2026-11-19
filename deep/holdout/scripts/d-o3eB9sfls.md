# Predicted script: 3Blue1Brown, "Why is pi here? And why is it squared? A geometric answer to the Basel problem"

- Channel: 3blue1brown
- Video id: d-o3eB9sfls
- Target duration: 1028 s (17:08)
- Recall risk: **vague**. I have a faint sense that this video involves light and distance, but I do not recall its structure, timestamps or wording. I built the beat sheet from the channel report (arc in section 2, moves in section 3, new principles in section 5) plus general knowledge of the Basel problem (the sum of 1/n^2 equals pi^2/6; Euler's sine-product proof; inverse-square intensity; the identity that the sum over all integers n of 1/(x-n)^2 equals pi^2/sin^2(pi x)). The specific physical device (lights spaced along a line, observer between them) is my own choice, made because "a familiar physical object that makes a 1/d^2 appear" is what the report's Home-first and toy-world rules predict. The exact geometric mechanism in beats 9-13 is the least certain part.

## 1. Predicted beat sheet

| Time | Lvl | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | hook-paradox, hook-question | Adding 1 + 1/4 + 1/9 + ... one more term at a time; it settles near 1.645; that is pi squared over six, and nobody looking at fractions would guess a circle constant lives here. Why pi? Why squared? | Running sum with bar chart of partial sums creeping toward a line; digits of pi^2/6 appear beside it |
| 0:50 | H | roadmap, honest-caveat, you-could-invent-it | Names the Basel problem; says there are many proofs, Euler's famous one is algebraic; this video follows a geometric one where the circle is visible; promises it is a tour of a clever idea more than a derivation to memorise | Title card, then a ghost of a circle fading behind the sum |
| 1:40 | H | toy-world, brute-force-first, visible-repetition | Add 10 terms, then 100, then 1000: the sum crawls (error shrinks like 1/N); can see it is near 1.64 but nothing in the arithmetic points to pi | Three numeric runs stacked, error column shrinking slowly |
| 3:00 | N | commit-to-answer, hook-question | Poses the wall: sums of fractions do not contain circles, so a circle must come from somewhere else; asks what physical thing makes a 1/d^2 appear | Sum on left, blank "?" on right |
| 3:40 | H | analogy, design-it-yourself | Light dims as one over distance squared: a lamp twice as far gives a quarter the brightness; draws the spreading wavefront to say why | A lamp with expanding spheres, same light spread over 4x, 9x area |
| 5:00 | N | act-it-out, special-case-first, toy-world | Stands an observer on a line with lamps at distances 1, 2, 3 on one side; brightness reading adds up to the Basel sum | Dot-and-lamp number line with a live brightness meter |
| 6:40 | N | minimal-definition-then-refine | "Total brightness" named as the quantity we want; for now the lamps sit only on one side and only at whole-number spots | Meter labelled with the sum, lamp spots highlighted |
| 7:30 | B | design-it-yourself, multiple-decompositions | Tries rearrangements: all integers both sides, only odd spots, only even spots; notes the odd-only version is the easiest to relate to the full sum | Three lamp layouts side by side |
| 9:00 | N | named stepping stone, notation-after-concept | The "almost Basel" quantity: lamps at every odd position on both sides of the observer; states it is the target for the circle | Lamps on both sides, meter reading highlighted as "almost" version |
| 10:00 | N | act-it-out, special-case-first | Moves the observer; watches the meter as a function of position; this function repeats every two steps and blows up at lamps | Observer slides, graph of brightness vs position grows and repeats |
| 11:30 | N | generalize-to-other-domains, simulation-as-argument | Shows the key move: bend the line into a circle; the evenly spaced lamps become evenly spaced points and the repeating pattern becomes rotation by angle; pi enters as the circumference | Line wraps into a circle; angle marker sweeps |
| 13:00 | N | meta-lesson-named, claim-before-derivation | States in words what the circle fact says: total brightness equals a simple function of the angle, no sum needed | Single clean statement on screen, then lamp animation |
| 13:50 | I | notation-after-concept, formula-read-as-procedure | First symbol appears: the sum over all integers written compactly; read as "for each lamp, add the inverse square of its distance" | Sigma notation replacing lamp animation, symbol by symbol |
| 14:40 | N | build-and-verify | Plug in observer at the midpoint: only odd distances left; total is pi squared (then divide by 4 for odd-only); numeric check against the running sum | Calculator-style check lining up |
| 15:30 | N | recap, notation-compaction | From odd-only to all: the even terms are one quarter of the whole sum, so three quarters are odd; algebra yields pi squared over six | Three-step algebra with colours matching lamp groups |
| 16:10 | H | callback-to-hook, failure-shown / honest-caveat | Returns to the opening: pi is there because the sum secretly describes a circle; squared because light dims as distance squared; caveats that the final pieces are skipped and links to Euler | The first sum with a circle drawn around it |
| 16:50 | H | teaser-next | Points to related ideas (other values of zeta, other proofs) and a sponsor or credit line | End card |

(Beat count 17, mean spacing about 60 s. Dense in 5:00-12:00 where new ideas arrive.)

## 2. Full narration script

Take the sum one over one squared, plus one over two squared, plus one over three squared, plus one over four squared, and keep going forever. Each fraction is a perfectly ordinary number. One. A quarter. A ninth. A sixteenth. Slowly they shrink, and slowly they pile up. Let me add them one at a time. After two terms the total is one and a quarter. After three it is a little over one point three six. After ten, about one point five four. After a hundred, one point six three five. And if you let a computer run for a long while, the total creeps up on one point six four four nine and never goes past it.

Now here is the strange part. That number is pi squared divided by six. Pi, the thing about circles, shows up inside a pile of unit fractions that has no circle anywhere in sight. And it is not pi that appears but pi squared. So there are really two questions. Why pi? And why is it squared?

This is called the Basel problem, and it stumped the best mathematicians for most of a century before Euler solved it. His argument is algebraic and gorgeous, and a lot of people will tell you that is the whole story. What I want to do here is something different. I want to show you a way to see the answer where the circle is actually on screen, so that the pi stops being a coincidence of algebra and starts being something you can point to. Fair warning, this is a tour of one beautiful idea, not a full formal proof from nothing, and I will be upfront about the steps I wave my hands over. And if you pay attention to the order of things, you might find that you could have come up with much of this yourself.

Before anything clever, let us be as dumb and honest as possible, because that tells us what we are up against. Add ten terms. You get about one point five five. Add a hundred, one point six three five. Add a thousand, one point six four three nine. See how slowly it moves? Every time I ten-fold the work, I only gain about one more digit. And look at those numbers. If I handed you one point six three five and asked where it comes from, nothing in it screams pi. It is an almost-number that only reveals itself in the limit. Brute force is going to tell us that the sum converges to something near one point six four five, and it is simply not going to tell us why.

So the arithmetic hits a wall. Fractions do not have circles inside them. If a circle is hiding here, it has to come from somewhere else, from some other picture that happens to produce the same sum. So let me ask the question the way an inventor would. Where in the physical world does the square of a distance, in the denominator, naturally show up?

Here is one answer you already know. Stand in a dark field with a lamp. Move twice as far from it and the light looks four times dimmer. Three times as far, nine times dimmer. Why? Because the light leaves the lamp and spreads out over the surface of a growing sphere, and the area of that sphere grows with the square of its radius. The same light, thinner and thinner. So brightness goes as one over distance squared. That is the one place where a one over n squared is not a trick, it is just how light works.

So let us build a toy world out of that. Picture a long straight road. You stand at one spot, and there are lamps along the road at distances one, two, three, four, and so on, all the same bulb, all the same power. The nearest lamp is at distance one, so it contributes a full unit of brightness. The next lamp, at distance two, contributes a quarter. The one at three contributes a ninth. And your eyes, or a light meter, just add up what all of them give you. Do you see it? The total brightness you read off is exactly our sum. One plus a quarter plus a ninth plus a sixteenth, forever.

That is a nice reframing, but it has not solved anything yet. All we have done is trade a pile of fractions for a pile of lamps. What it gives us, though, is a thing we can move around. We can change where we stand, add lamps on the other side, remove some of them, and ask how the total brightness responds. That is the sort of thing you can play with, whereas the bare sum you can only stare at.

Before moving on, I want to flag how much freedom we have here, because it is the important lesson of this stretch. Nothing about the original problem said anything about lamps, or roads, or standing in the dark. We chose that story. The sum is the fixed thing, and the story is a costume we are free to try on and take off. The reason this costume is a good one is that it is something we have good instincts for. You can imagine walking toward a lamp and watching it get brighter. You cannot imagine walking toward a fraction.

So let us play. Suppose we put lamps on both sides, at every whole-number distance. Because the left side mirrors the right, the total is exactly twice the Basel sum. Now suppose instead we only put lamps at the odd distances, one, three, five, seven, and so on. That is a different sum, one over one squared plus one over three squared plus one over five squared. Why would we ever want that? Because it turns out to be much more natural to relate to a circle, and because it is easy to relate back to the thing we really care about. Hold on to that thought, and I will come back to it in a few minutes.

Let me give this simpler quantity a name. I will call it the almost-Basel sum: the total brightness when lamps stand at every odd distance on both sides of you. It is almost the thing we want, and getting from it to the real thing will be a short step at the end.

Now watch what happens as I slide you along the road. When you stand exactly at the midpoint between two lamps, the nearest lamps are each half a step away. As you drift toward a lamp, that lamp gets absurdly bright, and the total shoots up toward infinity. Walk past it and it comes down again. And because the lamps are evenly spaced, the whole picture repeats: the total brightness as a function of your position is a pattern that goes up, spikes, comes down, and repeats, like a wave with sharp peaks.

A repeating pattern should make you suspicious. What do repeating patterns usually have to do with? Circles. Going around a circle is the most natural way to repeat. So here is the move. Take that infinite straight road and bend it into a circle. Every lamp that was spaced evenly along the line is now spaced evenly around the circle. The place where you stand moves around the circle too. And now the repeating pattern is not a mystery, because when you go all the way around you are back where you started.

Here is where pi arrives, and I would like you to see it arrive rather than take it on faith. Once the road has become a circle, how you measure position is by an angle. Going once all the way around is two pi of angle, or equivalently the pattern repeats when your angle has changed by a fixed amount, and that fixed amount is a fraction of pi. Every time the lamps spread out evenly, the way the brightness changes is controlled by that angle. So the pi was not hiding inside the fractions at all. It was hiding in the fact that evenly spaced lamps along a line repeat, and repeating is what circles are.

Let me say the main claim in plain words before I show you any more of the picture. The total brightness from the whole infinite row of lamps is exactly the same as something you can read off from a single angle, with no infinite sum at all. If that sounds too good to be true, it should; so let me convince you with the most extreme case. Stand exactly halfway between two neighbouring lamps. Then every lamp is at a distance that is a half, three halves, five halves, and so on, on both sides. Those are odd multiples of a half. Their squares are odd squares over four. So the total brightness, up to a factor of four, is the sum of one over odd squared, doubled because there are lamps on both sides.

And the circle says what that total is: pi squared. Not approximately. Exactly. Notice the two ingredients. Pi comes from the circle, from going around once. And the square comes from two places that are really the same place: the light dims as the square of distance, so the sum is a sum of squares, and when you ask how that depends on angle you end up with the square of the same circle number. Squares in, squares out.

I am going to write this down now, because this is the moment where a symbol is worth having. We have a picture we understand, so notation can just be shorthand for it. Instead of drawing lamp after lamp, we write a big capital sigma, which means add up, and under it we say which lamps: every whole number n on the road, positive and negative. For each such lamp we add the thing that lamp contributes, which is one over the square of how far it is from you. That is the entire formula. If you can picture the lamps, then you can read the symbols, and if you cannot read the symbols, go back to the lamps.

Notice what I did not do. I did not hand you the symbols first and ask you to believe them. You already watched the lamps and the meter, and the sigma only compresses that. When I say the sum over n, I mean walk along the road, visit every lamp, and add its contribution. Nothing more. If at any point the notation feels like a wall, picture the road again, because the road is the idea and the symbols are just its shorthand.

Let us check this against the arithmetic we started with. At the midpoint the formula says the total is pi squared. Take the lamp contributions at distances a half and three halves and five halves, square them, add both sides, and you get four times two times one plus a ninth plus a twenty-fifth and so on. Run it, and the total heads toward nine point eight six nine six. Pi squared is nine point eight six nine six. It is not a coincidence and it is not close, it is the same number. That is the best kind of check there is, because we built the picture first and never aimed at the answer.

Now let us come back to the Basel sum, the one over every square, not only the odd ones. How do we get from the almost version to the real thing? Think of all the whole numbers and split them into odd ones and even ones. The even ones are two, four, six. Two times anything. So one over an even number squared is one over four times a whole number squared. That means the even part of the sum is exactly one quarter of the whole sum. Therefore the odd part is three quarters of it. And we just found what the odd part is: pi squared over eight, after dividing out the doubled sides and the factor of four.

So three quarters of the Basel sum is pi squared over eight. Multiply both sides by four thirds, and the Basel sum is pi squared over six. The six that was hiding in the answer is a three from the odd-even split and a two from the two sides of the road. It was never mysterious. It was bookkeeping applied to a picture.

Pause here and run the checks yourself if you like. With the lamps only on one side you get the Basel sum, one point six four four nine. With lamps on both sides you get double that. With only odd positions on one side you get about one point two three three seven, which is pi squared over eight. Three numbers, three simple relations, all agreeing with the claim from the circle. If any one of them were off, the picture would be wrong, and it is not.

Let me go back to where we started. Why is pi here? Because a sum of evenly spaced things, repeated forever, is secretly something that goes around a circle, and any circle brings pi with it. And why is it squared? Because light dims as the square of distance, so every term in the sum is already a square, and the circle's version of the same fact gives you the square of the same number. A pile of fractions that looked like pure arithmetic was a picture of a circle all along.

I should be honest about what I have skipped. I pointed to the circle and described what it does, but I did not prove that the brightness function is exactly what I claimed; there is a rigorous reason, and it comes from how the pattern relates to itself when you zoom, but I have left it out. If you want the airtight version, Euler's original argument and several modern ones are linked below, and they are worth chasing. The thing to carry away is the shape of the argument: when a sum refuses to give up its secret, find a physical picture that produces the same sum, and then let the picture show you the symmetry the numbers hid.

And there is more waiting for you. The same sum with cubes does not give pi to anything nice, nobody knows why, and that fact alone should tell you how special the squares are. Even powers all give circles. Odd ones, as far as anyone knows, do not. If you try the picture yourself with the lamps, you might find some of that out before I explain it.

## 3. Rule trace

| Beat | Report claim that drove it |
|---|---|
| 0:00 hook | Sec. 1: one concrete object plus paradox; principle 1 (familiar start, 10/12); hook-question 9/12 and hook-paradox. The pi teaser (HEfHFsfGXjs) is "sell the question". |
| 0:50 roadmap and caveat | Sec. 3: honest-caveat 12/12, roadmap 11/12; arc step "roadmap with an honest caveat"; you-could-invent-it (calculus 0:34, Bitcoin 0:03). |
| 1:40 brute force | Sec. 2 arc step; brute-force-first 6/12 (calculus 2:54 rectangles); visible-repetition (pi teaser 100, 10^4, 10^6). |
| 3:00 wall | Arc: "a wall, or a need"; principle 11; new principle 2 (patch chain, failure drives the next piece). |
| 3:40 lamp analogy | Principle 4 (analogy then rigor, 9/12); design-it-yourself 10/12 ("what physical thing would make this?"). |
| 5:00 toy world | Toy-world 8/12; special-case-first 9/12 (radius 3 before R); act-it-out 8/12. |
| 6:40 minimal definition | Minimal-definition-then-refine 7/12. |
| 7:30 rearrangements | Calculus 1:59 multiple slicings; design-it-yourself. |
| 9:00 almost-Basel | New principle 3: named stepping stone, then diff (Fourier "almost Fourier transform" 7:35). |
| 10:00 slide the observer | Ghost-hands note (sweep a parameter until alignment); act-it-out. |
| 11:30 bend into circle | Generalize-to-other-domains 9/12 and calculus 8:35; simulation-as-argument 7/12. |
| 13:00 claim in words | Report section 7 orchestrator rule: "claim in words" before long derivation; Sphere shadow 1:29; new principle 7 (name the meta-lesson at the pivot). |
| 13:50 sigma | Principle 2 (symbol cost 11/11); notation after concept 10/12; Fourier first symbol at 12:37 of 19.7 min (about 64%), so first symbol roughly 80% in; new principle 4 (formula read as procedure). |
| 14:40 numeric check | Build-and-verify 8/12 (sphere shadow 6:51); Putnam "check against known answer". |
| 15:30 algebra | Notation-compaction; recap 9/12; staging of reading symbols as steps. |
| 16:10 callback | Callback-to-hook 9/12; ending type per report. |
| 16:10 undercut / caveat | New principle 6 (undercut your own story) and principle 5 (lower the bar, promise return, e.g. calculus 9:29). |
| 16:50 teaser | Teaser-next 9/12. |

**Report claims I could not turn into a concrete choice (too vague):**
- "Notation is held back and then framed as compression": gives no threshold for when; I chose a fraction (about 80%) by interpolating from Fourier transform and neural net data, not from a rule.
- "Humor appears in 6 but is light": no placement rule; I put none.
- "Pace by idea rate": no number of concepts per minute; I just made beats 40-70 s in the middle.
- "Persistent scene / colour contract": no guidance on which persistent object; I picked lamps without a report-based reason.
- The report gives nothing about the specific mechanism of a math proof; the geometric details are from outside knowledge and are the biggest risk.
- No data on sponsor or credit placement for videos of this era.
- Whether a real learner turn (pause-and-ponder) is used in pure-math videos: report says "at best" pause prompts, so I included one commit-to-answer line only (3:00), with low confidence.

## 4. Explicit predictions

- **First question to viewer:** about 0:35-0:50, the "why pi, why squared" pair (hook). A second, design-it-yourself question about where 1/d^2 appears at about 3:00.
- **First notation / formula:** the numeric sum is on screen from 0:00 (it is the hook object, written as fractions), so the first *new* symbol (sigma) appears about 13:00-14:00, roughly 80% in. If the critic counts the opening fractions, answer "0:00, but as an object not notation".
- **Misconception:** yes, a soft one: that sums of fractions have nothing to do with circles, so pi here is a coincidence of algebra; also possibly that Euler's algebraic proof is "the" explanation. Not a Veritasium-style planted wrong belief with a commit step.
- **Brute force first:** yes, around 1:30-3:00, adding up terms numerically and seeing slow convergence.
- **Examples:** about 3 numeric runs (10, 100, 1000), then a physical model that grows 1 lamp -> a few lamps one side -> both sides -> odd-only -> circle; 3-4 observer positions. One running object (lights on a line) carries most of the video.
- **Hook type:** paradox (surprising constant in a plain sum) plus a direct question.
- **Ending type:** callback to the hook (why pi, why squared), plus honest caveat about the skipped step, plus a soft teaser/hand-off to other proofs or related values.
- **Five moves most confident will appear:** (1) honest-caveat, (2) roadmap, (3) special-case-first, (4) notation-after-concept, (5) callback-to-hook. Next tier: brute-force-first, design-it-yourself, generalize-to-other-domains, teaser-next, build-and-verify.
