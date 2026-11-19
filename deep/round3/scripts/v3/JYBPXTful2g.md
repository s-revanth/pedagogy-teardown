channel: SebastianLague
id: JYBPXTful2g
title: Blender Character Creation: Texturing
duration: 952s (15:52)
condition: v3
recall: vague
exemplars read: deep/corpus/compact/TPEmonfLo94.txt, deep/corpus/compact/Q9f-WVs3ghI.txt

## Content skeleton
- Open on a personal story: the rigged character still looks like grey clay, and a first paint attempt was a mess.
- Set the scene: the mesh and rig from earlier parts, and a plain grey material.
- Explain UV unwrapping as flattening the surface so a 2D image can wrap onto it.
- Mark seams in edit mode, unwrap, and tidy the islands in the UV editor.
- Create the texture image, paint in texture paint mode, and watch the strokes appear on the model.
- Show a seam bleeding problem and how a margin around each island fixes it.
- Add a normal map for surface detail, then close on the finished look and a teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Story: the rigged character still looks like grey clay, and a first paint attempt was a mess |
| 0:40 | toy-world | Current state: mesh and rig from earlier parts, plain grey material |
| 1:40 | definition | UV unwrapping: flattening a surface so a 2D image can wrap around it |
| 3:00 | derivation | Marking seams in edit mode and unwrapping |
| 4:50 | demo-sim | Arranging UV islands in the UV editor, scaling them to fit |
| 6:20 | derivation | Matching texel density across arms, legs and torso |
| 7:20 | definition | Creating the texture image and switching to texture paint mode |
| 8:30 | visible-repetition | Brush strokes repeated across the body, mirrored to the other side |
| 9:50 | failure-shown | Seam bleeding and stretched patches, then the fix |
| 11:10 | derivation | Normal map for surface detail without extra geometry |
| 12:40 | payoff | Finished texture in the viewport, character reads as a character |
| 14:40 | teaser | Next episode: the rest of the character pipeline |

## Narration
<<<NARRATION
When I first got this character to the point of having a rig and a mesh, I was quite pleased with myself. Then I looked at him properly, and he still looked like a grey lump of clay. Every surface had the same flat colour, and nothing about him read as skin, cloth or anything else. My first attempt at painting him went badly. I just clicked around the model and ended up with smears that didn't follow any shape at all. If you've ever tried texturing something by eye, you'll know how that goes. So in this part we're going to fix that properly, starting from the foundations, and we'll make him look like a character rather than a mannequin. A texture is just a picture, but the picture has to fit the model exactly, or every detail lands in the wrong place. We want the eyes on the face, the seams of the clothing on the seams of the body, and the colour of the lips on the lips. Getting that alignment right is most of the battle. We can make a quick sketch on paper, but the real test is always in the viewport. We'll be checking alignment constantly, so it helps to have a clear process from the start. We'll also keep an eye on the lighting, since the colours shift under different lights.

Let's begin where we left off. We have the mesh, we have the rig from the earlier parts, and we have a plain grey material on everything. The mesh is made of roughly 12000 faces, and the rig has 14 bones, so the geometry itself is in good shape. Nothing is wrong with it as such, but the surface has no information about colour yet. It's a bit like having a sculpture and no paint. We need a way to tell Blender which part of a flat image belongs to which part of the body, and that's where the real work starts. I'll explain each step as we reach it, and we'll keep the interface the same throughout, so the screenshots stay useful. We start in the UV editor, move to the viewport, and come back again as often as we need. We don't need to jump between tools very much, which keeps the workflow calm. If we switch between too many modes, we lose track of where the seams are, and then the whole job slows down.

The key idea is UV unwrapping. Think of the surface of the mesh as something we need to flatten out, a bit like peeling the skin off a balloon and laying it on a table. If you try that with a real balloon, it tears, and the same thing might happen to a mesh if we're careless. Once it's flat, we have a 2D layout that we can paint on with a normal image editor. When the texture is applied, Blender wraps that flat picture back around the three dimensional shape. Every point on the model has a matching point on the flat layout, and that matching point is called a UV coordinate. The letters U and V are used because X, Y and Z are already taken by the model.

Now, we can't flatten a closed shape without tearing it somewhere. That's the reason we mark seams. Seams are the edges where the surface is allowed to be cut, so the unwrap can open the mesh up into a flat piece. We go into edit mode, select the edges we want to cut, and mark them as seams. For a character, it helps to put seams in places where they won't be seen, such as the inside of the arm, the back of the legs, or under the chin. I usually mark around 6 to 8 seams for a figure like this, and I try to keep each one short and easy to hide. We're basically hiding the cuts, and the best place for a cut is one that nobody looks at. We can also check each seam by looking at the mesh from the outside and the inside. If a seam sits in the middle of a visible face, we move it. Think about where the eye naturally travels, because the eye notices seams in the wrong place very quickly. We'll mark them, unwrap, and look again, and we repeat that until the layout feels right. It's not a perfect process, but it works well in practice.

With the seams in place, we select the whole mesh and unwrap it. The UV editor opens up and shows us the pieces, which Blender calls islands. At first the islands tend to be in a messy pile, with some very large and some very small. I usually spend a while here, because a clean layout makes the painting so much easier. We can move the islands around, rotate them, and scale them so that each part gets a fair share of the space. Anything important, like the face, should get the biggest share. About 25 percent of the sheet is a reasonable target for the head, and we can adjust from there.

In the UV editor, we also want to check the proportions. If the islands are scaled differently, a detail like an eye will look huge on one part of the body and tiny on another. So we select the islands for the arms and the legs, and we scale them so their texel density matches the torso. Texel density sounds like jargon, but it just means how many image pixels cover a given area of the surface. If the torso gets 2 pixels per millimetre, the arms should get 2 as well. You'll notice the difference as soon as the texture goes on, and I learned that the hard way on an earlier model.

Once the layout is tidy, we need a texture to paint on. We create a new image in the UV editor, and we give it a sensible size. I'm going to use 2048 by 2048, which is large enough for detail on the face and small enough to stay responsive while we paint. Then we switch the viewport into texture paint mode. Blender now shows the image on the model, and any strokes we make are written straight into that image. This is the moment where the character starts to look like something other than clay. Even a single stroke changes the feel of the model, and we can see it immediately. I always keep a second window open with the texture preview, so we can compare the two side by side. Every change in the paint shows up on the model right away. That tight loop is the reason texture paint feels so good to use, and I think it's the reason so many people enjoy it once they try it.

We pick a brush, set the radius and the strength, and start on the skin. The first strokes are rough, and that's fine. We can build colour up in layers, so a light pass comes first and then a darker shadow on top. Usually I'll do three passes, and each pass is a little more confident than the last. Because we're using X mirror, anything we paint on one side of the face is copied to the other, which saves a lot of time. You can paint half the face and let the mirror do the rest. We do the eyebrows, the lips and the cheeks in turn, and we check the result from several angles as we go. For a character like this, I usually start with the big, obvious areas, the skin and the clothes, and only then move to the small details. We can always add fine lines at the end, but it's much harder to fix a bad base layer later on. Let's keep the base layer simple and readable, because the details sit on top of it.

Now for the problem I mentioned earlier. When we paint right up against a seam, the colour can bleed across the cut, and that shows up as a faint line on the model. Sometimes a patch looks stretched because the island is squashed in the layout. We can see both problems here. The stretching comes from the UV scale, and the bleeding comes from the edges of the islands being too close together. The fix is to add a margin of about 4 pixels around each island, and then to rescale anything that looks distorted. It might look like a small thing, but it's the difference between a clean model and one that looks cheap. If you ever see a faint line like that, check the margin first.

So we go back to the UV editor, add the margin, and check the islands again. The stretched patch now looks like the rest of the body, and the seam is clean. We also use the texture preview to compare the layout to the model, which is a quick way to catch mistakes. That kind of checking matters more than it sounds. A small error in the layout can waste an hour of painting, and I've made that mistake more than once. About one in 5 of my first textures had some version of this problem, which is why I now check the layout before I paint anything.

There's one more layer we can add that changes the look a lot without touching the geometry. It's called a normal map, and it tells the shading how the surface bends at a fine scale. A normal map can make skin look pored, cloth look woven, or armour look dented, all without adding a single extra vertex. You don't need a heavy model for that, which is the whole appeal. We bake it from a higher detail sculpt, or we paint it by hand. Here we're going to keep it simple, and we'll use a normal map on the cloth and the face, so the light falls on them in a more natural way. Under the new normal map, the seams should be the only visible joins, so we check them again in the lit view. It takes about 10 seconds, and we can see the difference right away. If a seam shows a hard edge in the light, we go back and fix the UV margin. That kind of quick check saves a lot of time later, and we get a result we can trust. I'll set its strength to 0.6 so it doesn't overpower the colour.

We connect the normal map through an image texture node into the principled shader, and we set the colour space to non-colour data, because the values represent direction rather than colour. Then we look at the viewport in material preview mode. The change is immediate. If you look closely at the cloth, you'll see the light catch the edges of the folds, and the skin picks up a soft texture under the highlights. I counted the visible tones across one fold, and it went from one flat tone to about 3 distinct tones. Nothing about the shape has changed, but the character suddenly feels more like a person and less like a statue.

Let's step back and look at the whole result. We have a clean UV layout, a painted texture with mirrored details, a seam hidden where nobody will look, and a normal map adding surface detail. Each part is simple on its own, and together they do the job. The lesson I took from this is that most of the work happens before the first brush stroke, in the layout. If the unwrap is good, the painting almost takes care of itself. We spent about 70 percent of the time on layout, and about 30 percent on paint, and I'd make the same split again.

In the next episode, we'll bring these pieces together and set up the rest of the character pipeline, including the final materials and how the model is exported for the scene. We'll also look at a few shortcuts for repeating the texturing process on other characters. I have a rough plan for how that will go, and I think it's going to be a useful step, but we'll see how the export settings behave once we get there.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, Blender workflow with live viewport",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.12,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": null,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 1,
 "example_growth": "one seam, then the whole body, then normal map",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the grey clay character, reused as the before state",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 155,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "toy-world", "definition", "derivation", "demo-sim", "derivation", "definition", "visible-repetition", "failure-shown", "derivation", "payoff", "teaser"],
 "top5_moves": ["story", "toy-world", "visible-repetition", "failure-shown", "rule-list"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 155.00 (target 134.08-158.69, median 154.75)", "you_rate": "PASS 0.44 (target 0.37-0.6, median 0.51)", "i_rate": "PASS 1.22 (target 0.83-1.43, median 1.12)", "we_rate": "PASS 3.89 (target 3.86-5.9, median 4.81)", "num_rate": "PASS 1.60 (target 1.2-1.81, median 1.45)", "hedge_rate": "PASS 0.24 (target 0.18-0.34, median 0.25)", "example_rate": "PASS 0.05 (target 0.0-0.1, median 0.04)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "7/7 numeric targets pass"}}
```
