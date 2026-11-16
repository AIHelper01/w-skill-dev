# Teaching patterns and regression examples

These examples illustrate user-approved teaching routes. Adapt to the actual source; do not insert these topics into unrelated decks. Bold denotes original wording in the example, not a license to bold all new narration.

## First contents page

Now, let's take a look at what we're going to learn today.

Second, **Agent Planning: From ReAct to Reflection (optional).**

ReAct stands for Reasoning and Acting.

In this section, we will look at how an Agent plans tasks, breaks down complex problems, and improves its results.

This is an optional part of today's course, so I will only give a brief introduction.

Third, **Agent Action: Tools, MCP, and Skills.**

We will learn how Agents use tools, connect to external systems through MCP, and use Skills to complete specific tasks.

This is the key to moving from answering questions to taking actions.

Fifth, **Agent Engineering: Evolving Paradigms.**

We will explore three stages of AI engineering: Prompt Engineering, Context Engineering, and Harness Engineering. We will compare the differences between them and learn how to build more reliable AI Agents.

For a real first contents slide, include every chapter, not just these excerpts.

## Multi-column slide: computing, algorithms, data

Plan: 2020 column → 2022 column → 2025 column. Within each, title → representative product → two small effect boxes → large explanatory box. Do not move 2022 ChatGPT into the 2020 module just because the big box is at the top.

Example: First, let's look at 2020 — **Computing Power First.** A representative product was the **NVIDIA A100** GPU. What did this increase in computing power bring us? First, it helped **support larger AI models and more complex training.** Second, it helped **drive innovation in data processing, labeling, and synthesis.** Now, let's look at the blue box below. [Integrate the actual detailed source wording.]

## Timeline slide

Plan: each stage from left to right, with its dates, technologies and applications.

Then came the **1990s–2000s**, the **Rise of Machine Learning**. Instead of defining every rule by hand, we started teaching machines to learn from data.

The **Representative Technologies** included **Decision Trees** and **Support Vector Machines**. Support Vector Machines, or SVM for short, were among the most widely used machine learning methods at that time.

The **Representative Applications** included **Recommendation Systems** and **Spam Detection**. For example, a model could learn from existing emails and identify whether a new email was spam.

## One technology per question

For a timeline on Function Calling, MCP and Agent Skills, ask how the model requests an external action. Read the dated Function Calling entry and its original definition in bold. Then use one concrete example: the model selects a weather function and supplies Shanghai as an argument. The application runs the function and returns the result.

Use the remaining problem to introduce the next entry: how can several applications connect to the same tools? Follow with the dated MCP entry and its definition. Then ask what tells an Agent how to complete a recurring task and introduce the Agent Skills entry. Keep the original comparison together and move on with a short cue such as “Let's start with Function Calling.”

When a revised script is pasted after the wrong slide image, recover the new narration using its heading and put it directly after the matching slide caption. Remove any displaced duplicate heading or superseded narration after verifying the selected version.

## Capability hierarchy

For the four-level AI use example, explain bottom to top: 6 billion → 2 billion → 20 million → 5,000. Pair numbers with their exact source labels. If they are illustrative, say “These numbers are just examples. What really matters is how people use AI at each level.” Never represent illustrations as measured statistics.

## Important actions

**TODAY: HIRE IT → DIRECT IT → APPROVE IT → STOP IT**

**HIRE IT.** Choose the right AI Agent for your task.

**DIRECT IT.** Tell the Agent what you want to achieve.

**APPROVE IT.** Review and approve important actions when necessary.

**STOP IT.** Stop the Agent if something goes wrong.

We want AI to work for us, but we must always stay in control.

## Mixed text and diagrams

For a slide with concept text on the left and two related diagrams on the right, build explicit pairs before writing. A suitable route is:

1. Definition or core idea → immediately explain the upper comparison diagram.
2. Reason or limitation → state what the comparison makes visible.
3. Process steps → immediately trace the lower loop diagram and its return arrow.
4. Summarize once and move to the next slide.

Do not finish all left-side text and then add a generic `图片解读` section that repeats both diagrams. If revising an existing script, move the useful diagram sentences into the paired modules and delete the former tail block.

## One figure with several matching explanations

On an Agent architecture slide, pair the purple Planning node with the right-column planning definition, then use the Shanghai example to show task decomposition. For Memory, pair the blue node's short-term label with the short-term sentence, then pair the long-term label with the long-term sentence. For Tools, connect the green node to the tool-use text, then follow Execute, Observation, and Feedback as one loop. Keep one full screenshot and weave in short cues such as “Look under the blue Memory box.” Do not group the whole diagram and the entire right column as two consecutive modules.

## One case across a technical diagram

For an Agent memory lecture, start with the Shanghai trip. Its budget, weather and hotel choice are useful for the current plan. A preference for quiet hotels near public transport may be relevant again. Once the class can explain the difference, follow the diagram: the Agent selects the preference, writes it to long-term memory, searches for it when planning a later trip, and reads it into the new context. Point out the source labels at their respective steps. Keep the concrete facts paired with their memory roles.

For a tool-call training example, trace instruction → input → output. The instruction describes the available tool and its arguments. The input is the weather request. The output shows the structured call. Point to the actual function name, location argument, and any boundary tokens in the sample, and explain what each marks. Close with a question the example leaves open: how can applications connect to different tools through a common interface?

## One analogy for several concepts

Use the same email scenario throughout an engineering comparison. Prompt Engineering is writing a clear email. Context Engineering is assembling the attachments and background the recipient needs. Harness Engineering is building the working environment with shared tools, processes, permissions, and feedback. Keep each part next to its original source definition. A subsequent coding example can make Loop Engineering concrete: run the program, inspect the result, fix the error, and retry until the tests pass or the configured limit is reached.

## Course closing

On a full-course closing slide, return to the opening question, then connect the chapter takeaways to the components that answer it. In a course on how a chatbot becomes an Agent, recall what planning, tools, memory, and the execution loop each add. Bring them back together in the original Agent model and end with one sentence the class can remember.

## Software demos: installation, interface, and provider setup

These partial before/after examples use Slides 19–21 of a CC Switch lesson. The classroom path uses Windows and Direct Mode in this example. Bold marks wording visible on the source slide. Each complete script still requires all slide-local source text, commands, captions, and the full screenshot.

### Slide 19 — Give learners a route through platform options

Before: Read the download sources, platform commands, and file extensions with equal emphasis.

After:

We'll use Windows in this exercise. On the download page, choose the Windows installer. **Download the .msi file and double-click to install.**

Once it's installed, we'll open CC Switch and find where it lists the providers for Codex.

Pass when the classroom route is clear and the complete script also covers the other platforms, installer types, and exact commands. Without a confirmed classroom platform, present the choices without assigning one to the class.

### Slide 20 — Use the interface to prepare the next action

Before: Ask learners to read the toolbar labels from left to right, then mention the active provider at the end.

After:

Find the **OpenAI Official** card. The blue **In use** badge marks the active provider in this screenshot. Now look at the upper-right corner for **⑥ Add Provider**. We'll use that button in the next exercise.

Pass when learners can point to the state indicator and the next control. Cover the remaining labels in the complete script and give important operations their own speakable units.

### Slide 21 — Pair the screenshot with the action and explain the result

Before: Describe the upper screenshot during the steps and repeat its caption in a separate section. Treat a normal test reply as confirmation of the model identity.

After:

In the upper screenshot, **Step 1–2: Select Codex and Add a Provider**. Follow the red arrow to the orange button. **Click + Add Provider. (fig. ①).**

Later, after the exact enable, restart, and test step, explain the expected result:

Once DeepSeek is active in Direct Mode, Codex sends the request directly to DeepSeek. We're still using the Codex interface and its Harness. DeepSeek is the underlying model in this configuration. How would we do this with a model on our own server? We'll use vLLM in the next exercise.

Pass when both original captions appear beside their associated steps in the complete script and the source prerequisite, five instructions, and configuration-file entries are covered. Keep routing conditional without evidence that the provider and mode are active. A reply is evidence of a response. Use provider state or available request evidence to support a stronger claim.

## Regression checks

- For the 2020/2022/2025 example, reject a script that introduces the 2022 ChatGPT paragraph under 2020.
- For the six-stage timeline, reject a script that groups all technology names in a top section and all applications in a bottom section.
- For a capability pyramid, reject a script that reads numbers separately from their labels or reverses the approved progression.
- For contents, reject a script that only lists titles or expands optional material into a full lecture.
- For a revision, reject an unnecessary rewrite of accepted wording.
- For a mixed text-and-diagram slide, reject a script that explains all text first and appends both diagram explanations at the end.
- Reject a revision that keeps both the integrated diagram explanation and the old generic `图片解读` block.
