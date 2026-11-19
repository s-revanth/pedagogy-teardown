# SebastianLague | JYBPXTful2g | Blender Character Creation: Texturing

- channel: SebastianLague
- id: JYBPXTful2g
- title: Blender Character Creation: Texturing
- duration: 952 s (15:52)
- condition: v2
- recall: vague (I recognise only that a Blender character series exists, not this part's content)
- class (step 0): over-10 min; format = devlog tutorial (screen-recorded art workflow; colon title but no E-number); answer not stated; craft problem (getting paint onto a 3D surface); topic = 3D art and texturing
- exemplars read: deep/compact/PGk0rnyTa1U.txt (I Spent a Week Making a Game about Vacuuming, 17 min) read in full for devlog voice

## Content skeleton
- Cold open: a grey head looks like a mannequin; texture is what makes it a character; 19 seams is the stake.
- Brute-force first: paint directly on the 3D model; the paint bleeds across the far side of the head (failure on screen).
- Minimal definition of a UV map as a flat picture of the surface; unwrap the head into about 14 pieces.
- Checker texture as the verification device; cheek fine, ear stretched; one seam moved and rechecked.
- Arm and torso with 2 and 3 seams; same checker each time.
- Caveat: not a professional texture artist; one approach, not the approach.
- Base skin layer, noise variation at about 15 percent opacity, eye and lip detail on the same map.
- Render comparison and lighting; a regret about seams changed after painting; final render; no teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Grey clay head reads as a mannequin; texture and seams are the problem; nineteen seams counted on one head. |
| 0:50 | toy-world | Model on screen: about 4,000 faces on the head, eyes and teeth hidden so the skin is the only thing in view. |
| 1:30 | brute-force | Paint directly on the model with a soft brush; it works briefly, then bleeds around the far side of the head. |
| 2:20 | definition | UV map defined minimally: a flat picture of the surface, each model point pointing to one picture point. |
| 3:00 | demo-sim | UV editor: seams selected, head unwrapped into about 14 pieces; the cheek now sits in one island. |
| 4:10 | definition | Checker texture introduced as the test: equal squares across the head mean an even unwrap. |
| 5:00 | demo-sim | Cheek squares fine; squares near the ear stretch; one seam moved behind the ear; checker rerun, stretch gone. |
| 6:10 | demo-sim | Arm with 2 seams and torso with 3 seams; checker run on each; expected faint seam line noted. |
| 7:20 | caveat | Not a professional texture artist; studios automate seams; this method is slow and visible, not the fastest. |
| 8:00 | demo-sim | Base skin layer; noise variation in warm brown at about 15 percent opacity; opacity swept by eye. |
| 9:10 | demo-sim | Eye and lip detail painted on the same unwrapped map so it lines up with the checked seams. |
| 10:00 | demo-sim | Three renders compared under the same lights: base, base plus noise, plus detail maps; any step not visible is removed. |
| 11:00 | demo-sim | Key light at 60 percent and fill at 25 percent; normal map adds pores and fine lines. |
| 12:00 | generalize | Same unwrapping logic applied to a shoe, a shirt or gloves; seams go where the fabric would fold or meet. |
| 12:50 | caveat | Regret: three seams changed after the skin was painted, costing most of an afternoon; plan seams first next time. |
| 13:40 | payoff | Final render with the checker removed; colour consistent across seams; the unwrap test passes. |
| 14:50 | coda | Closing: the shirt is next; thanks for watching. No teaser (not a series). |

## Narration
<<<NARRATION
Every painter knows the moment a flat wall starts to look like a picture, and for a character model that moment is the texture. Right now this head is just grey clay, and it looks like a mannequin, which is fine for a sculpt but not for a finished character. This video is about putting colour and detail onto the surface, and it's also about the one problem that makes texturing hard, which is the seams. We count nineteen seams on this head alone, and every one of them is a place where the paint can go wrong.

Let's start with the model itself. The head has about 4,000 faces, the arms and torso add a few thousand more, and the whole character sits in the viewport at a comfortable size. We've hidden the eyes and the teeth for now, so the skin is the only thing we're looking at. The first question we need to answer is how to get paint onto a three-dimensional surface without it smearing, stretching, or breaking when the camera moves around the character.

The obvious idea is to paint directly on the model, so that's what we tried first, with a large soft brush on the cheek. It works for about thirty seconds. Then the brush starts crossing an edge of the mesh, the paint wraps around the far side of the head, and the colour bleeds into a place where it shouldn't be at all. Nothing is wrong with the brush, so we're not going to blame it. The surface just doesn't have a flat place to put the paint, and that's the failure we need to fix.

The paint has to live on a flat image, and the model has to know which part of that image goes where. The mapping is called UV unwrapping, and the minimal definition I'll use is this: a UV map is a flat picture of the surface, with every point on the model pointing to one point on the picture. We don't need the whole theory yet. We only need a flat map that matches the surface closely enough that the paint lands where we expect it to land.

Let's look at the head in the UV editor. Each island on the flat map is a piece of the mesh, and the edges where the islands are cut are the seams. We'll select the edges we want as seams and then unwrap, which gives about 14 flat pieces for the head. The cheek, which was the problem before, now sits in one clean island, rather than being split across the far side of the head, and that's a much better place for it to live.

To check the unwrap, we use a checker texture. It's a grid of alternating squares, and every square should be the same size across the whole head. If a square is stretched, the unwrap is distorted in that region. If the squares change shape across a seam, the seam is in the wrong place. We'll run this check on the head first, then on the arm, then on the torso, using the same checker each time so the results can be compared directly.

On the cheek we see square squares, which is good. Near the ear they're stretched into thin rectangles, so the unwrap is too tight there. We'll cut a new seam behind the ear, unwrap again, and rerun the checker. The stretching drops away. This is exactly the kind of change we want to see directly, one edit at a time, rather than guessing from the final render, because the final render hides which edit did what.

Now the arm. The arm is a simple tube, so one seam along the underside should be enough. We make the cut, unwrap, and check. The squares are even along the length, and where the seam runs there's a faint line in the paint, which is expected. I'd rather have a line I can predict than a smear I can't. The torso is the same story, with a seam down the back and one under each arm, and the checker confirms each of them in turn. The arm has 2 seams and the torso has 3, which is a small number compared with the head. We want the seam to be predictable, so we place it where a shadow would fall anyway.

I want to be honest here. I'm not a professional texture artist, and the way I'm doing this is one approach, not the approach. Studios often use software to plan seams automatically, and some artists work from reference photographs and never use a checker at all. My method is slow and visible, which suits a video, and I'm not claiming it's the fastest route to a finished character.

Now the paint itself. We start with the base skin colour as one flat layer, then add a second layer for variation. The variation is a noise pattern in a warm brown at about 15 percent opacity, which breaks up the flat colour. It's the same idea as the noise we used in the terrain series. Too much and the skin looks dirty, and too little and it looks like a plastic toy, so we sweep the opacity and stop at the value that looks right in the viewport. For example, the cheek needs more squares than the back of the head, so the detail goes where the eye lands first.

Next are the details, which are the parts we need to get right to make a face look like a face. The eyes need a separate texture because they have a different material, and the lips need a slight shadow along the edge. We paint these on the same unwrapped map, so everything lines up with the seams we already checked. If I had painted them directly on the three-dimensional model, I would be back at the bleeding problem from earlier, and we'd lose an hour to it.

Here's a quick comparison we want to show. The first render is the flat base colour with no variation. The second adds the noise layer. The third adds the detail maps for the eyes and lips. The head is the same in all three, under the same lights, from the same camera. If the difference between two renders isn't obvious, I should remove that step, so every layer has to earn its place in the file.

Then lighting. A texture only looks right under light, so we add a key light at 60 percent strength from the upper left and a soft fill at 25 percent from the other side, and then check the skin again. We can tell the lighting works when the highlights match the light we placed. The highlights on the cheek and the forehead are where I'd expect them, and the shadow under the jaw looks natural. The normal map, which fakes small bumps on the surface without adding geometry, adds pores and fine lines that the flat colour simply cannot show on its own.

The same unwrapping process applies to other things as well. A shoe, a shirt, or a pair of gloves all need seams in the places where the fabric or the shape would naturally fold or meet. Once the seam logic is clear for one character, the rest of the wardrobe is mostly repetition, about 3 hours of work per garment in my rough estimate, and that's why I spent so long on the head at the start. The lesson transfers, and if you pick this up yourself, start with the head and use the same checker on any piece you make.

Let me also say what I'd do differently, because we learned that the hard way and will do it in a different order next time. We'd plan the seams before we start painting, because I changed three seams after the skin was already painted, and each change meant repainting part of the cheek. That cost me most of an afternoon, which is a lot of time for three lines on a mesh, and the file grew to about 300 megabytes, so you should keep an eye on it. Next time we'd check the unwrap with the checker before any paint goes on the model, even if the first version looks fine to the eye.

Now the final check. We render the head with the checker removed, with the full skin, the eyes, the normal map, and the lights in place. The colour is consistent across the seams, and we can see that clearly, and I can't find the places where the unwrap was tight, which was the test I cared about most. The face reads as a face, and the body parts match in tone, which was the last thing I worried about before the render finished.

That's where this character's skin sits for now, and we still have a lot to do with it. The first render took 4 minutes, and the final 4K render took about 20 minutes, the second took 6, and the third took 9, which is probably fair for a head. The arms and the torso have their own passes to come, and we'll keep the same checker running, using a 2048 by 2048 texture for the head and roughly half that for the arm, and the clothing is still grey clay, so there's plenty left to do. The shirt is next, and its seams are already worrying us a little. Thanks for watching.
NARRATION>>>

## Slots
```json
{
 "format_class": "devlog tutorial: adjacent classic problem with blow-up number, brute-force then unwrap, checker as build-and-verify",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.06,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.15,
 "first_notation_frac": null,
 "payoff_frac": 0.86,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "head -> arm and torso -> clothing",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "epistemic",
 "recurring_anchor": "the checker texture, reused on head, arm, torso and final check",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "beat_sequence": [
  "hook",
  "toy-world",
  "brute-force",
  "definition",
  "demo-sim",
  "caveat",
  "demo-sim",
  "generalize",
  "caveat",
  "payoff",
  "coda"
 ],
 "top5_moves": [
  "build-and-verify",
  "visible-repetition",
  "failure-shown",
  "brute-force-first",
  "toy-world"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 100,
 "median_beat_s": 50
}
```

```json
{"rule_trace": {
 "U1": "applied: devlog format gate (topic type devlog-tutorial); under-10 items n/a at 15:52; roadmap and callback withheld; recap off",
 "U2": "n/a: neither the title nor the first 40 s states the answer; the method comes after the failure",
 "U3": "applied: impact coda on the final render; no teaser (not a series); no hook callback",
 "U4": "applied: the checker texture is reused on the head, arm, torso and final check, each pass adding one change",
 "U5": "n/a: no symbols or formulas are spoken; terms such as UV and seam are introduced at the object they describe",
 "U6": "applied: narration at normal speech; beats of 30-60 s with silent screen runs, not a fixed grid",
 "U7": "applied: no roadmap, no vote, no planted misconception; the paint-on-model failure is shown, not announced",
 "U8": "applied: epistemic caveats: not a professional, one approach among several, studios automate seams",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a task (texturing), not an application or an end state",
 "C1": "applied: devlog tutorial format, not impersonal lecture and not a series lesson",
 "C2": "applied: one example (the same head) rerun with one layer per pass (base, noise, detail) under the same lights",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no published design source is named; the checker is a practical test, not a cited technique",
 "C5": "applied: opens with an adjacent classic problem (paint bleed and seams) and a human-scale blow-up number (nineteen seams on one head)",
 "D1": "applied: failure on screen (paint bleeds across the mesh; the cheek stretches near the ear)",
 "D2": "n/a: the repairs are named by their function (UV map, seam), not after the failure",
 "D3": "applied: one seam moved per pass and the checker rerun, so one edit is isolated at a time",
 "D4": "n/a: no honest-close bundle; caveats sit inline and the close is a final render",
 "D5": "n/a: no equation revealed after behaviour",
 "N1": "n/a: under-10 band rule; this video is over-10 min",
 "N2": "broken: 100 words per minute (measured), outside p25-p75 137-158; 1,600 words over 15:52 give about 101 wpm; the length cap and the silent screen runs keep the full-runtime rate low",
 "N3": "applied: 0.25 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.39 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 2.65 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.01 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.6 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.13 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.06 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "n/a: not a series; U3 withholds the teaser",
 "B3": "n/a: roadmap withheld; a devlog tutorial does not call for one",
 "B4": "applied: no spoken recap"
}}
```
