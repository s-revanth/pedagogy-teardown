# Channel: CGPGrey
- id: 8Fn_30AD7Pk
- title: Highway Numbers Aren't Names. They're Coordinates.
- duration: 510 s (8:30)
- condition: base
- recall: none

## Content skeleton
- Opens with the question of why a highway's number looks arbitrary until you know the system.
- States the answer up front: the numbers encode direction and position on a rough grid.
- Explains the odd/even rule for north-south and east-west routes, with I-5, I-95, I-80 and I-10 as examples.
- Toy grid of a country with main routes laid out, so the viewer can place each number.
- Sketches the history: a national network built in the 1950s, numbering settled to make navigation easy.
- Explains three-digit numbers: they are loops or spurs tied to a main route through the last two digits, with the first digit saying which kind.
- Examples: I-495 (a loop tied to I-95), I-285 (a loop tied to I-85), I-395 (a spur tied to I-95).
- Caveat that there are exceptions and that state and older routes follow other logic.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Why does a highway have a number that seems random? |
| 0:25 | answer-statement | The numbers are coordinates: direction and rough position, not names. |
| 0:55 | roadmap | One line: the odd/even rule, the grid, the three-digit rule, then the exceptions. |
| 1:15 | toy-world | Blank map with a grid; main routes drawn as lines; viewer asked to guess before the reveal. |
| 2:15 | viewer-turn | Pause and guess: which way would an odd number run, and which way an even one? |
| 2:40 | definition | Odd numbers run north to south, even numbers run east to west. Numbering rises from west to east and from south to north. |
| 3:45 | demo-sim | Place I-5 along the West Coast, I-95 on the East Coast, I-80 across the north, I-10 across the south. |
| 5:00 | story-rung | The network was laid out in the 1950s and the numbers were set to make a route easy to read at speed. |
| 6:00 | derivation | Three-digit rule: the last two digits name the parent route; first digit even means loop, odd means spur. |
| 6:50 | generalize | I-495 as a loop tied to I-95; I-285 as a loop tied to I-85; I-395 as a spur tied to I-95. |
| 7:30 | caveat | There are exceptions; older routes and state roads use their own logic. |
| 7:55 | payoff | A number is a coordinate that tells you roughly where you are heading. |
| 8:15 | callback | Back to the question about the number that looked random. |
| 8:30 | coda | End. |

## Narration
<<<NARRATION
Why does a highway have the number it has? Drive across a country and you will pass signs that look almost random. Two here, a five there, something with three digits and a loop that seems to go nowhere. It is easy to assume the numbers were handed out in the order the roads were built, or by a clerk with a list. In fact the numbers carry information. They are coordinates. They tell you roughly which way a road runs and roughly where it sits in the country.

Here is the outline. The odd and even rule. The grid that the rule creates. The three-digit rule for the loops and spurs. And then the exceptions, because there are always exceptions.

Start with the grid, since everything else depends on it. Imagine a country as a big sheet of paper, with routes drawn across it. Some run roughly north and south. Others run roughly east and west. If you were designing a system so that a driver could read the number and know the direction, you would want to split the routes into two families, and give each family a clear signal.

That is the rule. Routes that run north and south get odd numbers. Routes that run east and west get even numbers. Once you know that, a number tells you the direction before you even see the road.

Now the second part of the rule, which is about position. The numbers go up as you move across the country. For east and west routes, the numbers increase from south to north. For north and south routes, the numbers increase from west to east. So a route with a bigger number is further north or further east than one with a smaller number.

Let me place a few on a map, so you can see the logic before the reasons.

Interstate 5 runs north and south, and it is odd, which is correct. It sits along the West Coast, the western edge of the country. Its number is small because it is near the west. Interstate 95 also runs north and south, and it is odd. It sits along the East Coast, which is much further east, and its number is much bigger than the five. Both are odd because both run north and south. Their sizes differ because one is further west and the other is further east.

Now the east and west routes. Interstate 80 runs east and west across the north of the country. It is even, which is correct. Interstate 10 runs east and west across the south, and it is also even. Its number is smaller than the eighty, because the southern route sits below the northern one. The numbers rise as you move north, just as the rule says.

Stop for a moment and try it yourself. If you know a route is odd, which direction does it run? If you know a route is even, which way is it going? And if you know it has a larger number than another route in the same direction, where is it relative to that route? If you can answer those three questions, you have learned the whole core of the system.

Where did this come from? The national network was laid out in the 1950s, when the government funded a large new set of limited-access highways. Planners needed numbers that would work for drivers moving fast, reading signs from a distance, and trying to decide which way to turn. A simple grid meets that need better than a list of names. A name tells you nothing about where a road goes. A number that encodes direction tells you a great deal.

Now the three-digit numbers, which are the part that seems most mysterious. A three-digit interstate is not a main route. It is a branch of a main route. The last two digits tell you which main route it belongs to. So a three-digit number ending in five is connected to the five, and one ending in ninety-five is connected to the ninety-five.

The first digit tells you what kind of branch it is. If the first digit is even, the route is a loop, a bypass that goes around a city and comes back to the main road. If the first digit is odd, the route is a spur, a branch that leaves the main road and goes somewhere else, often into a city.

Let us check this against real examples. Interstate 495 ends in ninety-five, so it belongs to the ninety-five. Its first digit is four, which is even, and it is a loop that goes around Washington, D.C. Interstate 285 ends in eighty-five, so it belongs to the eighty-five. Its first digit is two, which is even, and it is a loop that goes around Atlanta. Now the odd case. Interstate 395 also ends in ninety-five, so it belongs to the ninety-five. But its first digit is three, which is odd, and it is a spur, a branch that leaves the main road and runs into the city. Each of those tells you two things at once: which route it hangs off, and whether it loops or branches.

Now the exceptions. The system is not perfect. Some routes were renumbered over the years. Some older roads were already numbered and kept their numbers. State routes follow a separate system, and different states have different habits. So when you find an exception, it is not a sign that the whole idea is wrong. It is a sign that the system was built on top of older history, and that history is still visible on the map.

So the payoff is simple. A highway number is not a name. It is a coordinate. It tells you the direction the road runs, roughly where it sits, and, if it has three digits, which main route it connects to and whether it loops or branches.

Go back to the sign you passed at the start. That number was not random. It was telling you where you were heading.
NARRATION>>>

## Slots
```json
{
 "format_class": "toy-grid decoding explainer: coordinate rule, map placement, three-digit branch rule",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": null,
 "payoff_frac": 0.93,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 6,
 "example_growth": "grid rule -> main routes I-5/I-95/I-80/I-10 -> loops and spurs I-495/I-285/I-395",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.3,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the odd/even rule (returns at 0:25, 2:40, 3:45, 6:00)",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 35,
 "beat_sequence": ["hook","answer-statement","roadmap","toy-world","viewer-turn","definition","demo-sim","story-rung","derivation","generalize","caveat","payoff","callback","coda"],
 "top5_moves": ["toy-world","analogy","visible-repetition","honest-caveat","hook-question"],
 "absent3_moves": ["act-it-out","inline-quiz","learner-discovers"]
}
```
