# SebastianLague / JYBPXTful2g

- Channel: SebastianLague
- ID: JYBPXTful2g
- Title: Blender Character Creation: Texturing
- Duration: 952 s (15:52)
- Condition: base
- recall: vague

## Content skeleton

- Starts from a finished textured character to show the target, then the grey model it came from.
- Plan: unwrap the model to a flat map, paint the colours onto that map, then set up the surface materials.
- UV unwrapping explained: flattening a 3D surface into 2D, with seams placed where the surface can be cut.
- Practises on a simple cube first, then applies the same steps to the character's head and body.
- Shows stretched or overlapping islands as mistakes, and fixes them by moving seams and islands.
- Paints base colours and skin tones in layers; compares a brute-force paint of the whole sheet with a more deliberate layout.
- Material setup: base colour, roughness and the difference between colour and surface response.
- Ends on a lit render of the finished character, with a short wrap-up.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Finished textured character shown first, then the grey model; claim that colour is the next step. |
| 0:40 | roadmap | Three steps: unwrap, paint, then material settings. |
| 1:20 | definition | UV map defined as a flat layout of the 3D surface; seams are where the surface is cut. |
| 2:20 | toy-world | A plain cube unwrapped first, so each face and seam is easy to see. |
| 3:30 | demo-sim | Seams marked on the character; unwrap run and the islands appear in the UV editor. |
| 5:00 | wall | Overlapping and stretched islands; the texture looks smeared on the arms. |
| 6:10 | brute-force | Paint straight onto the whole sheet without a layout; seams show up as colour jumps. |
| 7:20 | analogy | Like a sewing pattern: cut the garment into flat pieces so it can be laid out and coloured. |
| 8:10 | demo-sim | Base colours and skin tones painted in layers; the character gets its look. |
| 9:50 | misconception-defuse | A texture is an image placed by coordinates, not a colour stored on the model. |
| 10:40 | derivation | Material nodes: base colour feeds the surface shader; roughness controls how sharp the highlights are. |
| 11:50 | demo-sim | Render under a light, compare the matte and glossy areas, adjust the roughness. |
| 13:30 | recap | Unwrap, paint, then material; each step fixes a problem the previous one leaves. |
| 14:30 | coda | Final lit render held on screen, with a short closing line. |

## Narration

<<<NARRATION
So here is where we want to end up. A character with proper colours, skin that looks like skin, clothes that have a pattern, and a material that catches the light the way you would expect. Before we get there, I want to show you the model we are starting from. It is a grey shape. It has the right proportions and the right surfaces, but no colour, and no detail beyond the geometry. Everything you just saw as a finished render is the result of the steps in this video.

The plan is in three parts. First we unwrap the model, which means giving it a flat map. Then we paint onto that map. And finally we set up the material, which tells the renderer how the surface should respond to light. Each of those steps depends on the one before it, so it is worth taking them in order, even if it feels slower than just jumping in.

Let's start with the unwrap, because this is the part most people find confusing at first. A 3D model is a surface in space. A texture is a flat image. To put one on the other, you need a way to flatten the surface into two dimensions, and that flat layout is called a UV map. The U and the V are just the names of the two axes on the flat image. Every point on the model gets a pair of coordinates in that flat space, and the texture is sampled using those coordinates.

The catch is that you cannot flatten a closed shape without cutting it somewhere. Think of peeling an orange. You can get the peel flat only if you cut it into pieces. The cuts are called seams. So when we unwrap, we are really choosing where to put the seams, and then letting the software flatten each piece. The seams are a choice you make, and they matter a lot for how the paint behaves later.

I'm going to practise on something simple first. Here is a plain cube. It has six faces, so it is easy to see what the unwrap is doing. I mark a few edges as seams, run the unwrap, and the faces appear in the UV editor as a set of flat squares. You can see which edges are joined and which are cut. If you rearrange the squares, the cube still looks the same in 3D, but the texture would land on the faces in a different way. This is the same idea, with more faces, that we will use on the character.

Now the character. This is where it gets fiddly. I go through the body and mark seams in places that are hidden or naturally divide the surface. Under the arm, along the back, around the joints. Then I run the unwrap and look at the result in the UV editor. The islands appear, which is the name for each flat piece, and they are a bit of a mess at first. Some are much bigger than others, some are rotated oddly, and a few are sitting on top of each other.

Those problems are not just cosmetic. A stretched island means the texture will be squeezed in one direction, so a pattern on the arm looks wrong. Overlapping islands mean two parts of the body share the same pixels, so painting one part paints the other. I made both of these mistakes on purpose in the first pass here, and you can see the arm texture smear as soon as I put a test pattern on it. That is the wall. The fix is not to try harder with the paint. The fix is to go back and move the seams and rescale the islands until the layout is clean.

Before we go further, I want to show you the approach I tried first, because it is worth knowing why it fails. The brute-force version is to skip the layout entirely and paint straight onto the whole sheet, all in one go, without thinking about which bits are next to which. It seems quicker, and it works for the first few strokes. But once you get to the places where two islands meet, the colour jumps. A seam shows up as a visible line where the paint from one piece does not match the paint from the other. It looks like a bad join in a cheap piece of clothing.

I like a sewing pattern as a way to think about this. A tailor does not sew a jumper out of a single piece of cloth. They cut paper patterns, lay them flat, decorate each piece, and then join them. The unwrap is the pattern. The paint is the fabric. If the pattern is sensible, the finished garment fits. If the pattern is a mess, no amount of careful stitching will hide it.

So with a clean layout, we can paint. I start with the base colours in broad layers. First the skin, which is a warm, slightly desaturated tone, and then darker patches for the joints and the areas that would catch shadow. Then the clothing, which gets its own colour and a simple pattern. Each layer is a separate pass, so I can go back and change one without wrecking the rest. It is not a fast process, but the result starts to look like a character, and that is a good feeling.

And here is a misconception I had myself. I used to think that a texture was a colour stored on the model, as if each vertex had its own paint. That is not how it works. A texture is just an image, and the UV coordinates say where each part of the model samples from that image. The model does not carry the colour, the image does. Once that clicks, it becomes much easier to understand why seams and islands matter so much. You are designing where the image lands on the surface.

Now the material. The texture gives you colour, but colour is only part of how a surface looks. The material decides how the surface responds to light. In the node setup, the base colour from the texture feeds into the main surface shader. Then there is roughness, which controls how spread out the highlights are. A low roughness gives a sharp, glossy reflection, like a wet surface or a metal. A high roughness scatters the light, which is what you want for cloth and most skin.

I set up a simple material on the character and then render it under a single light. The difference between the matte and the glossy areas is very clear once you see it. I turn the roughness up on the clothes and down on a patch of skin, and you can see the highlights shift. It is a small change in the numbers, but a big change in how the character reads. This is the step that makes the paint look like a real surface rather than a flat picture.

The reason I like the material step so much is that it fixes problems the paint cannot. A flat colour under flat light looks like a sticker. Add roughness variation and the surface starts to look like it has some physical presence. Paint can make the colour right, but only the material can make it feel right under light, and that is why the steps come in this order.

I also want to be upfront that I am not claiming there is one correct way to do any of this. Different artists handle seams differently, paint in different tools, and set up materials in different ways. What I am showing is one sensible route. The principles are more important than my particular choices, and you should feel free to change any of the steps once you understand what each one is for.

Let's render the whole character one more time, under a proper light, from a few angles. Look at how the seams have disappeared, how the colours sit where they should, and how the matte and glossy areas separate. Every step we took was about one of those things. The unwrap made the layout clean, the paint made the colour right, and the material made it read as a surface.

So to recap. We unwrap to make a flat map, with seams placed where the surface can be cut. We paint onto that map in layers, and we check for jumps at the seams. Then we set the material so that the colour responds to light the way we want. Each step depends on the one before, and skipping any of them leaves an obvious gap.

And there we have it. A textured character that looks like it belongs in a scene. Thanks for watching, and I will see you in the next part.
NARRATION>>>

## Slots

```json
{
 "format_class": "tutorial, step-by-step, tool-driven",
 "answer_given_upfront": true,
 "hook_type": "spectacle-demo",
 "first_question_frac": 0.04,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.67,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "cube -> head -> full character",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.22,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the character's seam lines, referenced in each UV step",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 65,
 "beat_sequence": ["hook", "roadmap", "definition", "toy-world", "demo-sim", "wall", "brute-force", "analogy", "demo-sim", "misconception-defuse", "derivation", "demo-sim", "recap", "coda"],
 "top5_moves": ["build-and-verify", "brute-force-first", "failure-shown", "toy-world", "analogy"],
 "absent3_moves": ["inline-quiz", "expert-dialogue", "second-person-role"]
}
```
