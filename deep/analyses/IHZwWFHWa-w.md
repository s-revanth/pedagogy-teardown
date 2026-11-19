# Gradient descent, how neural networks learn (3Blue1Brown)

**Arc.** Recap of the network (0:04-1:52), goal and setup (1:52), the cost function as scolding (3:22), a dimension ladder for descent: 1 input, 2 inputs, 13,000 (5:06-8:33), name and meaning of the gradient (10:17-12:02), layer-stack recap (12:22), performance and the surprising failure of the edge story (13:09-16:17), homework and resources (16:33), interview extension (17:26).

**Strongest moves**
1. *Show the full complexity, then zoom (4:30-5:25).* He states the cost function takes 13,000 inputs and says that is too much to imagine, then shrinks to one number in and one out.
2. *Dimension ladder (5:06-8:33).* The ball rolling downhill carries from the 1D slope sign, to the 2D negative gradient, to a column vector of weights. Same algorithm, bigger space, so effort stays low.
3. *Lowering the bar (8:00).* Tells the learner they only need to know a downhill vector exists and will be okay without multivariable calculus.
4. *Second reading of the gradient (10:33-12:02).* Components give relative importance of each weight, with a 3-to-1 example, an alternative to spatial direction that works when dimensions can't be pictured.
5. *Failure shown (13:09-16:17).* Hidden neurons look random, noise gets confident answers. This undercuts the edge story from the previous video and he says so.

**Unusual.** Most explainers end on success. This one ends on what the network does not do, then hands the learner a prompt (16:33) and an expert clip about memorization. Cost function is introduced emotionally ("bad computer") before the math at 3:41.

**Principle verdicts.** 1 confirmed. 2 confirmed. 3 not observed. 4 confirmed. 5 confirmed (scolding, shoes). 6 confirmed. 7 partly. 8 partly, no speech-rate evidence. 9 confirmed. 10 confirmed. 11 confirmed. 12 confirmed. 13 confirmed.

**Velocity implications.** Build a reusable dimension-ladder scene. Have the voice state what the learner need not master. After teaching a method, run a failure-case beat so the mental model is not overclaimed. Eval: does a tutor ever show where its own earlier motivating story breaks?
