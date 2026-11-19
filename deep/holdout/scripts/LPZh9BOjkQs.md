# Predicted script: 3Blue1Brown, "Large Language Models explained briefly"

- Channel: 3blue1brown
- Video id: LPZh9BOjkQs
- Target duration: 478 s (7:58)
- Recall risk: **vague**. I know this is a short, general-audience overview in the same family as the channel's neural-network and transformer series, and I have a faint sense of an "imagine a script" style opening, but I cannot recall its beats or wording. I deliberately built from the report plus general subject knowledge (next-word prediction, pretraining, parameters, backpropagation, RLHF, GPUs, transformers and attention). Note the report has no data for a short overview: the closest report items are the pi teaser (hook and caveat only) and the Transformers video's preview-first move (3:06), so predictions about compression are extrapolated.

## 1. Predicted beat sheet

| Time | Lvl | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | hook-paradox, toy-world | Imagine a movie script: a conversation between a user and an AI assistant, with the assistant's reply torn off. If you had a machine that predicted what comes next, you could finish the script, and that is what a chatbot is | A script with a missing last line, cursor blinking |
| 0:45 | N | minimal-definition-then-refine, special-case-first | Defines an LLM as a function that predicts the next word, but gives probabilities for every possible word, not one word; chatbot picks from them | A word box with a ranked list of candidate words and percentages |
| 1:30 | N | simulation-as-argument, honest-caveat | Appending the chosen word and repeating gives a whole answer; picking sometimes less-likely words makes outputs differ run to run; so the same prompt gives different replies | Text growing word by word; same prompt run twice with different results |
| 2:15 | N | roadmap | Preview: training on huge text, tuning with human feedback, then the architecture (transformers) | Three-step list lights up in order |
| 2:35 | B | analogy, visible-repetition | Scale of training data: a human reading nonstop would need thousands of years; parameters as dials on a giant machine | Stack of text sources; a wall of dials/numbers, initially random |
| 3:30 | N | act-it-out, design-it-yourself | Random dials give gibberish; show a text, hide the last word, compare the machine's guess to the real one, nudge the dials so that word becomes likelier; repeat on trillions of examples | Training example, predicted vs actual, tiny dial adjustments |
| 4:40 | N | honest-caveat, approximation-gets-less-wrong | Backpropagation is the algorithm for the nudging; nobody sets the parameters by hand; the scale of computation is beyond comprehension; only possible on GPUs | Dial wall zooms out to huge scale; a GPU icon, big number |
| 5:25 | N | story, minimal-definition-then-refine | Pretraining makes a good autocomplete, not a good assistant; refine with human feedback: people flag unhelpful responses and parameters are tuned toward preferred ones | Two candidate replies, a thumbs vote, dials shift |
| 6:10 | N | roadmap, show-full-complexity-then-zoom | Transformer: words become lists of numbers; attention lets words update each other based on context so "bank" shifts with surrounding words; layers repeat | Word vectors, arrows between words updating meaning |
| 7:10 | N | honest-caveat, undercut-own-story | Behaviour emerges from parameters tuned by the training process; researchers cannot say exactly why a given word comes out; so results can be surprising | Dials and output, question mark over the middle |
| 7:30 | H | callback-to-hook, teaser-next | Returns to the torn script; points to the longer deep-learning series and transformer videos; invites the viewer to go deeper | The torn script now completed word by word; end card with links |

(11 beats, mean about 43 s, consistent with a compressed overview where every beat is a New idea and the ladder is thin.)

## 2. Full narration script

Imagine you happen upon a short movie script that describes a scene between a person and their AI assistant. The script has what the person asks, but the last part, the assistant's reply, has been torn off. Now imagine you also have a very clever machine that can read any piece of text and predict what word comes next. Then you could finish the script. Feed the machine what is already on the page, let it guess the assistant's first word, then the next, and the next, until the reply is complete.

That is, at heart, what is going on when you chat with a large language model. It is a mathematical function that takes in some text and predicts what word comes next. When you type a question to a chatbot, the program quietly wraps it into something like that script, and then asks the machine to fill in the assistant's part.

Here is a detail that matters, though. The model does not hand back one word. It assigns a probability to every possible word that could come next. Maybe one word is forty percent likely, another is fifteen percent, another is a few percent, and thousands more share the tiny rest. The chatbot then picks from that list. Often it takes the likeliest, but it does not always, and a little randomness is mixed in to make the writing feel more natural. Then it adds the new word to the text, and asks again. One word, another, another, and a whole answer unspools.

This also explains something you may have noticed. Ask the same question twice and you might get two different answers. The model itself is deterministic, it gives the same probabilities every time, but the choosing step has a bit of dice in it, so the two stories drift apart.

Pause on how strange that is for a second. When you ask a chatbot something, it feels like it understands you and is composing a thought. What is actually happening is a single repeated move: look at everything so far, produce a list of likely next words, pick one. All the apparent intelligence has to live inside how good those lists are. And those lists can only be good if the machine has absorbed an enormous amount about how people write, argue, explain and joke. So the interesting question is not what the loop is, since the loop is simple, but where the quality of the lists comes from.

Now there are really three things to understand: how it learns to predict, how it is turned into an assistant, and what is inside the machine that does the predicting. Let us take them in that order.

First, learning. The model is trained on an enormous amount of text, much of it scraped from the internet. The amount is hard to feel. If a person read nonstop, around the clock, it would take them many thousands of years to get through what was used to train one of the largest models. And what is the machine that learns from it? Picture an enormous panel of dials, really just numbers, called parameters. The way the model behaves is completely determined by the values of those dials. These systems can have hundreds of billions of them.

At the start, the dials are set at random, and the model is useless. Feed it the beginning of a sentence and it produces gibberish. So here is how training goes. Take a snippet of real text, hide its final word, and let the model guess. Compare its guess to what the real word was. If it gave the real word only a tiny probability, nudge every dial a little so that the true word becomes slightly more likely next time. Then do the same thing with another snippet. And another. And you do this for trillions of snippets. The nudges are tiny, but they add up, and slowly the dials settle into values where the model is good at predicting text it has never seen before.

The algorithm that works out which way to turn each dial is called backpropagation. I will not go into it here, but I want you to notice something about it. No one sits down and chooses the value of those hundreds of billions of numbers. They are shaped by the training process, from the data, by a rule that only says: be a bit better at predicting the next word. How much computation is that? If you could do one billion additions and multiplications every second, it would take well over a hundred million years to do all the operations involved in training the largest models. It is only possible because of specialized chips called GPUs, which can run huge numbers of these operations in parallel.

But learning to predict internet text is not the same thing as being a helpful assistant. A model that has only done that is a good autocomplete. Ask it a question and it might continue with another question, or with an argument from a forum. So there is a second stage. Humans look at the model's answers, and they flag the ones that are unhelpful or wrong, or prefer one over another. Those preferences are used to tune the parameters again, nudging the machine toward the kind of answers people actually want. The first stage gives it knowledge about the language, the second stage gives it manners.

So what is the machine doing inside? For years the dominant design was one that read text word by word, in order. A newer design, called the transformer, changed that. Instead of going one word at a time, it takes in all the words at once. First, each word is turned into a long list of numbers that encodes something about its meaning. Then comes the key idea, which is called attention. It lets the lists of numbers talk to each other and refine their meaning based on context. Think of the word bank. In one sentence the lists around it nudge it toward a place where you keep money, and in another toward the side of a river. The numbers for the same word end up different depending on its neighbours. Then this whole process, attention plus a second kind of processing step, is repeated over and over, layer after layer, until the last list of numbers is used to produce those probabilities for the next word.

I want to be honest about one thing. I have described the structure and the training process, but not why a particular word comes out of it. The behaviour is not designed by anyone. It emerges from the values of those parameters as they were tuned. So even the people who build these systems cannot tell you in detail why the model chose the word it chose. That can make the results surprising, in good ways and bad ones, and it is a big reason why they are an active area of research.

If it helps to hold the whole thing in your head, it is three ideas stacked together. A function that outputs probabilities for the next word. A huge set of dials tuned by trillions of tiny corrections. And an architecture, the transformer, that lets words in context reshape each other's meaning. Everything else is scale and engineering.

So come back to the torn script. Now you can see that the final reply is not retrieved from anywhere. A machine tuned on mountains of text, and then refined by people, is guessing the next word, again and again, from a list of probabilities, until the page is full. If you want to see the details, I have longer videos on how neural networks learn and on how transformers and attention actually work, and I think you will find that the pieces fit together more simply than it might seem.

## 3. Rule trace

| Beat | Report claim |
|---|---|
| 0:00 hook | Sec. 1: one concrete object held on screen; principle 1 (familiar start); hook-paradox; toy-world 8/12 (pi teaser 0:04 for compressed hook). |
| 0:45 minimal definition | Minimal-definition-then-refine 7/12 (neural net 2:39 "a thing that holds a number" -> later function); new principle 3. |
| 1:30 repetition, variability | Simulation-as-argument 7/12; honest-caveat 12/12. |
| 2:15 roadmap | Roadmap 11/12; Transformers previews pipeline at 3:06 before background (preview-first). |
| 2:35 scale analogy | Analogy 8/12; principle 4. |
| 3:30 training | Act-it-out 8/12; design-it-yourself 10/12; neural-net ch.1 gradient and cost beats; Gradient descent video (cost as a scolding). |
| 4:40 backprop and compute | Honest-caveat; deferred rigor to links (sec. 6, "defer rigor to links or sequels"). |
| 5:25 RLHF | Patch chain (new principle 2): pretraining failure motivates the second stage. |
| 6:10 transformer and attention | Dependency order; show-full-complexity-then-zoom (3 occurrences); Transformers colour contract. |
| 7:10 emergence | New principle 6 (undercut your own story); honest-caveat. |
| 7:30 ending | Callback-to-hook 9/12; teaser-next 9/12; sec. 6 "closing often open". |

**Report claims I could not turn into a concrete choice (too vague):**
- No data at all on the short overview format; I cannot tell whether the channel keeps the full arc (brute force, wall, stepping stone) in 8 min. I dropped brute force and notation, extrapolating from the pi teaser being "hook and caveat only".
- "Pace by idea rate": no number; I chose 11 beats.
- "Hope before mechanism" gives no guidance about when to skip it for time; I did not include an explicit hope beat.
- Misconception-first appears 4/12 with no pattern for when; I left it implicit.
- No report claim on sponsor, link or credit placement.
- "Persistent scene" notion has no specific content for this topic.

## 4. Explicit predictions

- **First question to viewer:** none in the first minute as a literal question; the opening is an "imagine" setup. I predict the first explicit question at about 2:00-3:00 ("what is inside the machine?"), with low confidence.
- **First notation / formula:** none. No equation at all; at most a probability list (percentages), which is a chart, around 1:00.
- **Misconception:** partial. That a chatbot looks up or retrieves stored answers (or that it is a fixed program of rules); resolved by the next-word probabilities. Not set up as a long planted-and-broken misconception.
- **Brute force first:** no. The nearest equivalent is the random-dials gibberish stage (a failed starting state), at about 3:30.
- **Examples:** one running example (the torn script / chat), plus 1-2 short ones (the "bank" word sense, a snippet with its last word hidden). Growth: from one word predicted -> a full reply -> trillions of training snippets (scale jump rather than a ladder).
- **Hook type:** scene / thought experiment (imagined torn script), not a paradox question.
- **Ending type:** callback to the opening script plus teaser to longer videos in the deep-learning series, with an honest caveat that the inside is not fully understood.
- **Five moves most confident will appear:** (1) honest-caveat, (2) minimal-definition-then-refine, (3) roadmap, (4) teaser-next, (5) callback-to-hook. Next tier: analogy, recap, act-it-out (training loop).
