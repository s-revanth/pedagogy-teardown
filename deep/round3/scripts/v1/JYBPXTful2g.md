# Header
- channel: SebastianLague
- id: JYBPXTful2g
- title: Blender Character Creation: Texturing
- duration: 952 s (15:52)
- condition: v1
- recall: vague

## Content skeleton
- Goal: give a low-poly character a skin: colours, detail and small surface features.
- Toy world: a cube with a checker texture, so distortion is visible at a glance.
- First attempt: paint directly on the 3D model in the viewport; the paint smears and stretches.
- Minimal definition of UV coordinates: a flat cut-out of the surface, with seams where it is cut.
- Unwrap the cube, check that the checker squares stay square.
- Unwrap the head with seams placed behind the ears and under the jaw.
- Misconception: one giant texture for the whole body is not required; separate islands are fine.
- Generalise to eyes, clothing and accessories; visible-repetition on texture resolution.
- Honest caveat that the paint is not realistic skin; teaser for rigging.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Finished character with skin on screen; the model needs a surface to paint on |
| 0:30 | roadmap | Unwrap the surface, then paint on the flat map |
| 1:00 | toy-world | Cube with a checker pattern in the viewport |
| 2:00 | brute-force | Paint straight onto the 3D model in the viewport |
| 3:00 | wall | Stretching and seams on the sides of the head |
| 4:00 | wall | Checker squares distorted along the curved faces |
| 5:00 | definition | UV map as a flat cut-out of the skin; seams are the cut lines |
| 6:30 | demo-sim | Unwrap the cube; checker squares come back square |
| 8:00 | demo-sim | Unwrap the head with seams behind the ears and under the jaw |
| 10:00 | misconception-defuse | One big texture is not needed; separate islands are fine |
| 11:00 | generalize | Same workflow for eyes, clothing and accessories |
| 12:00 | demo-sim | Texture resolution swept at the same camera angle |
| 13:30 | caveat | Paint is not realistic skin; shading needs more work |
| 14:30 | recap | Three steps: unwrap, check, paint |
| 15:00 | teaser | Next: rigging the character |
| 15:30 | coda | Sign-off |

<<<NARRATION
This is the finished character. It has a skin, with colours, a bit of detail around the eyes and mouth, and some small features that catch the light. The model underneath is just a shape, and the skin is a picture laid over it. So how do you put the picture on the shape? That is what this episode is about.

Here is the plan. First we make a flat version of the surface, then we check that it is not distorted, then we paint on the flat version. Painting straight onto the model is the dumb way, so we will try that first.

The toy world is a cube with a checker pattern. I chose a checker on purpose. Squares are easy to judge by eye, so if the texture is stretched or pinched, you can see it at a glance. Before anything else, I want the checker on screen, because it is the test I will keep coming back to.

The first attempt is the dumbest one. Paint straight onto the three-dimensional model, in the viewport, and see what happens. It is quick, and on a flat face it looks fine. The paint follows the surface, and you get a nice clean stroke. So far, so good.

Then I move onto the curved parts. The sides of the head are where it falls apart. The paint smears, the checker squares stretch, and there are visible seams where one bit of paint meets another. In the viewport it looks like I am painting on a moving target, because the surface is turning under the brush. That is the wall. Painting on a 3D surface directly does not give you a clean result.

So here is the failure in close-up. The checker is distorted along the curved faces. Squares that should be square are long and thin on one side, and squashed on the other. It is not a painting problem. It is a mapping problem. Each point of the model has to point at a place in a flat image, and the mapping I have is badly behaved on the curves.

Now the definition. A UV map is a flat cut-out of the skin. Imagine peeling the surface off the model and laying it flat on a table. Where you have to cut, you get a seam. A seam is simply a cut line, and the flat layout is the map. That is the entire idea, and you do not need any more machinery than that to start.

Let's test it on the cube, because the cube is easy to check. I unwrap it, and the flat layout appears in a second window. Then I look at the checker on the model again. The squares come back square. Each face has its own piece of the layout, and the cuts are at the edges where the faces meet. That is the check I wanted: the checker is the proof that the map is good.

Now the head. This is harder, because a head has no simple flat faces. I place the seams behind the ears and under the jaw, where they will be hard to see. Then I unwrap, and the layout is one large connected piece with a few islands where the cuts are. I look at the checker on the model. It is still a bit stretched near the top of the head, so I move one seam and unwrap again. That is the loop: unwrap, look at the checker, move a seam, repeat. The checker tells me when to stop.

Here is a mistake I made early on. I thought the whole body needed one giant texture, with every part of the body in the same flat picture. You do not need that. Separate islands are completely fine, as long as each island has its own piece of the image and the seams are placed sensibly. Splitting the layout into islands can make the image easier to paint, and it does not hurt the result. I was trying to save effort in the wrong place.

With the head unwrapped and the checker square, the paint goes on the flat layout, not the model. I paint the skin tone, then the detail around the eyes and the mouth, and then I look at the model. The paint lands in the right place. The stroke that looked messy on the curves is now clean, because I am drawing on a flat surface that the computer wraps back onto the model.

The same workflow works for the eyes, the clothing and the accessories. Each one gets its own unwrap, its own seams, and its own checker test. You do not need a new method for each thing, just the same three steps: unwrap, check, paint. That repetition is why I like it. Once the first part is working, the rest is the same procedure.

Then there is texture resolution. A higher resolution gives sharper paint and more detail, and it costs memory. I sweep the resolution at the same camera angle, from low to high, and look at the same area each time. At low resolution the detail is soft. At higher resolution the eyes are crisp. Past a certain point, the extra pixels are invisible from a normal distance. So I pick the lowest one that looks right at the distance the character is shown.

Now the honest bit. This paint is not realistic skin. A real face has subsurface scattering, pores and fine lines, and I am not modelling any of that here. Shading would need a lot more work, and I have not done it. What I am showing is the mapping and the workflow. The skin on the screen is a rough illustration, and it is good enough to show the process, but it is not a finished look.

So here is the recap. Unwrap the surface into a flat layout. Check it on a checker so you can see distortion. Paint on the flat layout, not on the model. Those three steps are the whole method. Everything else is detail on top of them.

Next time we will rig the character, which means putting a skeleton inside the model so it can move. The seams and the layout will matter then too, because a bad mapping shows up again when the body bends. For now, the checker has to be square.

If you try this yourself, start with a cube, and do not go on to the head until the checker is square on every face. Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, tool walkthrough",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.13,
 "first_notation_frac": null,
 "payoff_frac": 0.78,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "cube -> head -> eyes and clothes",
 "roadmap": "one-line",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the checker pattern, checked after every unwrap change",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 60,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","misconception-defuse","generalize","demo-sim","caveat","recap","teaser"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","build-and-verify","generalize-to-other-domains"],
 "absent3_moves": ["hook-paradox","inline-quiz","expert-dialogue"]
}
```
