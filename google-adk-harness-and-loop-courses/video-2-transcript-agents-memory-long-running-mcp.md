<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Video 2 transcript (agents, memory, long-running, MCP)

> **TL;DR:** Raw Whisper transcript of the 72-minute compilation: ADK first agent, three memory layers, long-running agents, MCP and multi-agent basics.
> **Source:** https://x.com/ryouxbt/status/2116158187745247638  ·  **Project:** evolve-lab  ·  **Updated:** 2026-11-02

Raw Whisper turbo output, with mishearings: "JEPA" is GEPA, "self-involving" is self-evolving, "everyone 8" is everyone_ate. Timestamps: `~/Videos/X/ryouxbt/2116153759415828480.srt`.

So you're going to learn what AI agents are, not just in theory, but in practice. We'll look at
the ideas behind modern agents, and then we'll build your very first AI agent step-by-step
using Google's ADK. By the end, you'll understand how agents reason, act, and adapt, and you'll
have code that you can actually run yourself. So what are AI agents? At the simplest level,
an agent is software that doesn't just answer, it can decide and take action. Instead of generating
a single response like a traditional chatbot, it looks at your request, figures out what steps
need to be taken, maybe calls an API, runs code, looks at the results, and then decides what to do
next. One of the clearest explanations comes from the research paper React, synergizing, reasoning,
and acting in language models. The idea in that paper was simple but powerful. Language models
shouldn't just generate text in one go. They can actually reason step-by-step, take an
action like calling a tool or API, observe the results, and then decide what to do next.
That cycle of reasoning, acting, observing, and adjusting is the foundation of how modern
AI agents work. And it lines up with how it's defined. Systems with reasoning, planning, and
memory. With enough autonomy to adapt and make decisions on behalf of the user. Now, not all agents
behave the same way. A useful way to think about them is in three broad patterns. First, we have
sequential agents. These run step-by-step like an assembly line. Step one, then step two, then step
three. They're predictable but rigid. Second, we have reactive agents. These decide in the moment. They look
at the current state and ask, what should I do next? Maybe tool A one time, tool B the next. They're
flexible but they don't plan ahead. Lastly, we have deliberate or planning agents. These pause to
sketch a plan, then execute. Think about booking travel. You don't just buy a flight randomly. You
pick dates, hotels, and then that's the order of steps that you follow through. So which of these is
the right one for you? It depends on the problem. For simple, predictable flows, sequential is fine.
For dynamic, reactive works better. And for multi-step goals with dependencies, you want planning agents.
Okay, that's the high-level view. Now, let's actually build an agent so you can see these ideas in action.
We'll build a blog writing agent. You give it a topic, it will generate a structured outline, turn that
outline into a full blog post, and then suggest alternative titles and hooks. This is where ADK's
categories comes in. As we walk through the code, notice how the planner and writer agent are LLM
agents, which are powered by a model. They're wrapped in loop agents, which are workflow agents in ADK.
These handle retries automatically if validation fails. And if we ever wanted something beyond that,
ADK would also let us extend a custom agent by subclassing the base agent. So let's set up the
environment and then go line by line through the code. First off, you need to install UV. You can do
that by running the command right here. Secondly, you need to install Google ADK because we need to
obviously use ADK in this. And then let's create a file called agent.py in your IDE. We need to
import these key libraries, and then we can start building out our very first agent. So the first
agent that we're building out is called the blog planner. Its only job is to take a topic and turn it
into a structured outline. We give it the name blog planner, so it's easy to identify, and we tell it
which model to use, which comes from our environment file. The description is just a human readable note.
The important part of the introduction is here we actually tell it what to produce, which is a markdown
outline with a title, a short introduction, four to six sections with bullet points, and a conclusion.
By spelling that out, we make the output much more reliable. Finally, look at the output key. We set it to
blog outline. This means whatever this agent writes will be stored in shared state under that name so
that the next agent that can pick it up can do it automatically. Next, we add a second agent, the
outline validation checker. This one doesn't write anything new. It just checks the outline. Its
instruction is strict. If the outline and state has a title, an intro, four to six sections, and a
conclusion, it must answer with the word okay. If something is missing, it must answer with the word
retry and explain what's wrong. That way we can automatically decide whether to accept the outline
or try again. To connect the planner and the checker, we've wrapped them inside a loop agent called
robust blog planner. The loop first runs the planner, then the checker. If the checker says,
okay, we're done. If the checker says retry, the loop runs the planner again with the same instructions.
It can do this up to three times. This gives us a safety net so if the model forgets something,
it has another chance to get it right. Now, we create another agent called blog writer. This one
takes the outline we just saved in blog underscore outline and turns it into a full markdown blog post.
The instruction tells it how to write. It should assume the audience is software engineers, skip
the basics, and focus on practical insights, explain both the how and the why, and include short quote
snippets where helpful. It should also follow the structure of the outline with proper headings.
The finished draft is saved under blog underscore post in shared state. Ready for the next step. Next up,
we're going to add another checker, this time for the post. It's called blog post validation checker.
It looks at blog underscore post and checks if the article has an introduction, sections that match
the outline, a conclusion, and clear explanations. If it passes, the checker says, okay. If not,
it says retry and list the fixes which are needed. Just like with planning, we combine the writer and its
checker into a loop agent called robust blog writer. This makes the system automatically retry the
writing step until the validation passes up to three times. Now we wrap each loop, the robust blog
planner and the robust blog writer as tools. This is what lets the root agent call them directly without
worrying about what's happening inside. Finally, we put it all together with the root agent called
blogger. The instructions for blogger are simple. When a user gives it a topic, first it calls the
planner tool to make an outline. Then it calls the writer tool to draft the full post. And finally,
it adds three alternative titles and two tweet length hooks. The root agent only has access to the two
tools we exposed, the planner and the writer. So its workflow is clear and controlled. You give it a topic,
it plans, it writes, it checks, and then it gives you a polished blog post. You've now successfully
written your first agent script. The next step is to actually run it. Head into your terminal and launch
it using this command with ADK web so you can view everything inside a simple UI. Once that's running,
open the local ADK web link in your browser and start interacting with the agent directly. To kick things
off, I'm going to ask it to generate a blog on the top 10 use cases for AI agents. Let's see how it
plans, writes, and delivers the results. Your sub-agents will then work together to create a blog post.
And that's it. You've built and run your first AI agent with Google's ADK. We started from the idea of
what agents are, then walked through the code step by step and finally saw it come to life in terminal.
Thank you for watching. Check out the description box for all the resources and code mentioned in
this video. Check out this next video to learn how to connect your AI agent to an MCP server.
Hello, everyone. Welcome to this agent memory series where we're going to cover how to manage your
agent memory to build your personalized agent. So in the next three episodes, you're going to learn how to
give your AI agent real memory step by step. So in the first episode, we will start with short-term memory.
So the agent remembers what you said earlier in the same conversation. And then we will do a demo
where a trip planning agent forgets everything on turn two and then we fix it using the same ADK
session powered by a session service. And in the second episode, we will move from in-memory storage
to a database and build a simple user preference door so that the agent can remember things like
you're a vegetarian, even in a brand new conversation. And the third episode of the series,
we will build a long-term memory. We will use Vortex AI Memory Bank service so that the agent can remember
facts from past conversations, even from images, video, and audio, and automatically record them with
preload memory tool. By the end of the series, you will know how to build your AI agents that remember the
conversation, the past experience across time and media. All right, let's jump into the first episode
that we will cover what a session is and how to pass into between agents with agent short-term memory.
First, let's cover what a session really means. A session is one continuous conversation, like one chat
thread on your phone. So in ADK Web UI, it default uses in-memory session service. If you create a new
session, the agent behaves like it just met you every single time. It can't check the previous conversation
thread and see everything you said before. Let's see this memory loss example. At turn one, the user asks,
plan a two-day trip to Lisbon. And then the agent plans day one. Great. At turn two, the user says,
perfect, plan day two. But when we create a new session, the agent starts over. It forgets everything
we said in previous conversation, including the city, day one plan, and the user's interest. Now let's fix it
just by using the same session. And here we create one session and reuse it across multiple turns. And
now we ask the same question. And in turn three, you ask plan day two. Because it's the same session,
the agent can now look back at the full conversation and adapt the plan. Now you know the magic of the
session, let's take a look at these two important components inside the session. They are events and state.
So for events, this is like the transcript of every user message and every agent reply,
even the user's media input, like image data. So this gives agent context. It can read earlier messages.
And the second important component is state. You can think of this as a small sticky note
that the agent needs quick access to. Things like a restaurant name, a confirmation number,
or a chosen thing. Why do we need to use state? Because you don't want your model to reread 50
messages just to find one value. Instead, you can store it once and reuse it. You can take a look
at this table to learn more about it. All right, let's take a look at this example of how agents
communicate with each other with session state. You can take a look at the link on the screen or QR code
to find the source code. All right. So for this example, agent A finds a restaurant and then agent B
gives direction to it. So we tell agent A output only the name of the restaurant. And then we map
that output to a key like a destination. And now agent B automatically receives destination as a variable.
So this lets multiple agents collaborate without scrapping the entire transcript. So one thing
you really need to remember is you should never modify the session object directly in your tool code.
So if you do that, the change will not be recorded in the event log and the persistent service won't save
it later. Instead, you should use the context that ADK gives you tool or callback. So when you
write to context.state, ADK records the change with the event, so it can be stored and recovered when
we move to database and long-term memory. And you can take a look at the screen to see the correct way.
You can also use the link on the screen or QR code to find the source code. Now let's recap what we
covered in this episode. Firstly, a session is one conversation thread. An event is like transcript.
State is like a structured scratch node. So if we use in-memory session service, we use the same
session across multiple turns to avoid memory loss. And lastly, we need to write state through context,
so ADK can save it later. And this gives your agent short-term working memory like RAM. It's fast but
temporary. In the next episode, we will add persistence so that your agent can survive in an app restart and
still remember the user. All right, see you there. Bye!
Hello, everyone. Welcome back to this agent memory series where we cover how an agent remembers from
short-term memory to long-term memory. In the last episode, we built working memory with session and
state leveraging the ADK agent's short-term memory. And that worked well until the app restarts. Then
everything is gone. So today, we fixed two things. Firstly, we will make the chat itself durable by
switching to a database session service so the agent can continue via a laptop after a restart. And
secondly, we will add a user profile store for key facts like vegetarian or like museum. So even a new
chat next week can still remember the user's preference. By the end of this episode, you will see firstly,
how to plug in a persistent session service. And secondly, how to design a small user preference database.
And lastly, how the agent reads and writes that profile through the tools. All right, let's go to the
first part, how to make the chat doable with a database session service. So this is our first upgrade
from our last episode, persistent session. In the last episode, we used in-memory session service. And here,
we replace it with a database session service that writes to a database file or a real database like
Postgres. From now on, every user message, every agent reply, and every state change is saved to disk.
The benefit is very simple. If the app restarts and the user returns with the same session ID,
the session service loads the full history and the latest step. And the agent continues this conversation,
note that you can also use a link on the screen or the QR code to find the source code we're talking
about here. So here, we use helper function get or create session. It first calls get session. If it
exists, we resume. And if not, it will create session and start fresh. Here, you don't rewrite your agent
logic. You just swap the storage engine under the session service. ADK also offers other types of session
service, which are in-memory session service. That is what we used in last episode. It is fast,
but it's short-term. It clears on restart. And then we have database session service. You own the database,
so conversation survives restarts. And lastly, we have Vortex AI session service. It is managed on
Google Cloud. We will deep dive into this with Memory Bank in the next episode. In summary, the session
service is plakable and your agent logic can stay the same. And the second part of this video is to add
a user profile store for long-term personalization. And this user profile store is for important facts.
Persistent sessions helps you resume the same conversation. But when the user opens a new chat
with a new session ID, next week, there is no transcript to read. So we add a small database table
for preference. One row per user ID and preference key. These example keys can be dietary, favorite thing,
transport mode. We keep it small and structured, so it's easy to query and update. How does the agent
use this data? We give the agent two tools. The first tool is recall user preference. It reads all saved
preference for this user. And the second tool is save user preference. It inserts a new key or update an
existing key. And both tools get a context that includes the current user ID. So writes and reads are
tied to the right person. We also guide the agent with clear instructions. Firstly, recall first. At the very
start of the conversation, recall user preference. And then, personalize and plan. You can use whatever
you find. And certainly, present and learn. After planning, ask if there's anything new to save. And
lastly, save last. If the user provides a new fact, call save user preference before finishing. And let's put
it together and give it a try. If you take a look at the screen. At the turn one, first time user,
user says, can you help me plan a trip? The agent follows his instruction and call recall user preference
first. Nothing is fun. And then the agent propose a plan, then ask, do you have any preference that I
should remember? At turn two, saving a fact, the user says, please save that I am a vegetarian. And the
agent then calls save user preference. It gets an update successful message and confirm to the user
that the preference is saved. And then we simulate a restart. We stop the app. Memory in RAM is gone.
But our session is on disk. And our user profile is in its preference table. And new chat next week,
a brand new session ID. A user says, hi, I'm back. Can you plan a trip for me?
And then the agent starts by calling recall user preference. And now you can find the role with
dietary equals vegetarian and personalize it right away. And this proves two behaviors.
Persistent sessions let us continue an existing chat after a restart. The user profile stores let us
personalize a brand new chat for the same person. So you can also use a link on the screen or QR code to
find the whole demo. Let's wrap up what we covered in this episode. So we make the chat doable by
switching to a database session service. That means a restart doesn't break the conversation. We also add
a user profile store with two tools recall and save. So the agent can remember key facts across different
chat and different days. Next time we will go beyond structured preference and single chats. We will build
a memory bank that can archive entire conversations and even media, text, image, audio, and video.
And then search by meaning to bring back useful facts in a new chat.
And that's how your agent remembers the photo of that building or the audio clip from that live,
that I use the detail weeks later. All right, I'll see you in the next video. Bye.
Hello everyone. Welcome back to this agent memory series, where we cover how to manage your agent memory
to build a personalized agent. In the last two episodes, we cover shelter memory with session and state,
persistent memory solution with a database. And in this episode, we will build a long-term memory
that spans many conversation and even different types of input with text, images, audio, and video.
We will cover one, the difference between a session service and a memory service. And two, two memory
service options, a simple in-memory version for a quick test. And what has AI memory
bank service for production with safe storage and search by meaning? And three, how to ingest
entire sessions or direct media files into the memory bank and how to retrieve relevant facts
automatically in a new chat using preload memory tool. Before we build our personalized agent with
what has AI memory bank service, we need to understand two service roles. First is session
service that manages active chats and let you resume a live conversation. And second is memory service
that manages a long-term archive. It is the filing cabinet. We have two ways of using memory service.
The simple in-memory memory service, it is very good for quick local tests. It doesn't save across
restarts and use basic keyword search. With what has AI memory bank service, it saves to the cloud and
support semantic search. For example, a search for two field vehicles can find a note about a bicycle.
So in this episode, we will use what has AI memory bank service and what has AI session service
powered by agent engine that can extract facts using Germany and generate embeddings and also store meanings,
not just text. All right, let's start by setting up the memory bank. To configure the memory bank,
we set up an agent engine that powers it. During this configuration, we choose two types of models. One model
to extract facts from conversation and media and another model to embed those facts so that we can
search by meaning. We can also define topics to organize what we store, like user preference and
travel experience. It is important to remember that this is not just a table. It is a service that
process content, finds useful facts and makes them searchable. And now our agent has a long-term memory
backend. Once we have it set up, we need to find a way to save memories. Here, we can ingest memories
in two ways. The first way is to archive a full conversation. At the end of a session, we call add
session to memory. The memory bank process user messages, agent replies, image reference, video
reference and audio reference. It stores key facts. The second way is to upload facts directly. As you
can see from this code example, we can preload from a file. We can send an image, a video or an audio file
with some text context to generate and store facts directly. Even if those files didn't come directly
from a chat. Either way, we're building a long-term knowledge base that the agent can use later. And
once we have this knowledge base, we need to retrieve memories automatically. And we add preload memory tool
to the agent. It runs at the start of every turn. So every turn, before responding, the tool reads the
user's new message, runs the semantic search in the memory bank, gathers the most relevant facts, injects
relevant facts into the prompt. And the agent doesn't need special logic. The tool enriches the context
automatically. And let's test this demo. At session A, a user shares a photo of a historical building
and a short video of a C and a small audio note from a town. So we end the chat and add a session
to the memory bank with add session to memory bank. The engine extracts facts such as like historical
building, enjoy the coast and visited the town. And we simulate a restart and some time passing. In session B,
this brand new chat with empty state. The user says, based on what I shared before, picture, video and audio,
can you suggest a cultural destination? Before the agent replies, this preload memory tool searches a memory
bank and injects those facts. Preload memory tool finds memories like user likes historical architecture, enjoy seaside
areas, visit a town. The agent then recommends a destination that matches the historical architecture
and responds with a personalized suggestion. This is long-term multimodal recall in action. You can also
use a link on the screen or QR code to find the whole demo. Alright, to wrap up our three episode series,
we now have three layers of memory. One is session and state for working memory during a live chat. And two,
persistent sessions and a user profile that survive restarts and personalize new chats. And three,
a memory bank that archives full conversation and media, then searches by meaning to bring back useful
facts later. And with these episodes, now you can build your personalized agent that is consistent,
contact severe over days and weeks. So in the description of this video, you can also find the
links to the demos and setup steps. Try them and tell me what you want to build next. Alright,
I will see you in the future videos. Bye.
Our colleagues, Shubham and Eric, just this last week, they released a new blog post called
Building Long-Running AI Agents That Never Lose Context with ADK. And this is great. This is open
source. You can check it out. And what the tutorial really gives you is a new hire onboarding coordinator
agent using this long running agent pattern. This is something that could run potentially for weeks
and weeks. The way that it works is that the agent sends, you know, a new person that's onboarding a
welcome packet, it then pauses, it can pause for a long time, multiple days, while you're waiting on that
new employee to do things like sign their documents, you know, delegate, talk about, you know, the IT
provisioning. So maybe you have a sub-agent helping with that. You might be waiting another few days for
hardware delivery, right? We're trying to get them their laptops. And finally, they might get a
personalized day one schedule at the end of all of this. And you want to complete all of these steps
using your agents without losing any of your context. Now, I mentioned the importance of, you know,
memory, dormancy, multi-agent delegation, all of these same concepts apply here. This is a really
great blog post for just being able to get started with something a little bit more nuanced. Now,
you'll see a preview of it here. I've actually got this running locally. Let's kick off a fresh
onboarding case. I'm going to give it a name, an email, a start date, anything that it kind of
requires for us to get started. So what I'm going to do is click new case and fill in the new hire
details and then submit. So we're going to click start fresh case. We have our HR command center,
we have our employee portal. We can see that there's a few different pieces here. You can see
there's a number of actions, right? You have to sign your packet. You've got your hardware,
right? Well, that's not something available just yet. And you can see that we have sent the employee
welcome email. It's waiting for their signature. It's waiting for the next employee action. There's
an entire workflow that's in place here. So the agent has called our send welcome packet,
logging the ADK activity, and then it immediately stops. And it's now in really that dormant state.
This is a real deployment. You know, this container could scale. There's no polling loop,
no thread spinning, and it's just waiting for an external event. So we can now move on to signing
the packet, right? So on the employee portal, the new hire should be able to see their unsigned
onboarding packet. And when they're ready, they can go and sign it. So you can see that we have a
signed packet here, right? I'm just going to go and sign packet. You can see that we've got our ADK
wake, and then it's waiting on hardware delivered. So the key thing to watch there was the UI not,
you know, optimistically updating. It was waiting for the ADK resume turn to actually complete in the
backend before it shows us anything. And this is really intentional. It proves the long running
pattern is real instead of something that's faked. Once the signed packet appears, you know, we can see
the updated state on the HR panel, right? And it should say something along the lines of, you know,
the signature has been confirmed. So we see our signed packet has been confirmed. Great stuff.
And then it advances to, you know, the IT provisioning phase. So we need to then think
about confirming the employee's laptop delivery. And we can simulate the carrier webhook. You know,
in production, this would be a real delivery callback from your shipping provider hitting some API
endpoint. Here, the employee just clicks, you know, the confirmed laptop delivered. So maybe they just
got it in the mail, right? And you can see that our state has once again changed. And we've now got
different UI here, right? We've got our day one schedule. So just to recap that sequence, the hardware
delivery receipt appears, then it automatically transitions to that day one schedule. And that
ordering is very intentional. The agent runs the steps in the sequence that the state machine dictates,
and it can't be coerced into skipping ahead. So that's all great. Now, three things that make
this pattern different from that standard chatbot agent I keep bringing up is that durable memory
schema. State is an enum in a database. It's not just raw JSON chat logs in some vector store. There
isn't context pollution. So we shouldn't have token bloat after weeks of idle time. And second, we've got
that event-driven dormancy. The agent isn't, you know, continuously running between those pause gates.
It's fully at rest. It's sleeping. And third, multi-agent delegation. When the coordinator needed to
provision IT accounts, it didn't do it alone. It was able to delegate to a specialized sub-agent
and keep each agent targeted with the reasoning chain still being very clean. So this all looks
great. As a reminder, this is completely open source. We'll make sure to link you up to this
repo so you can go and you can check out the full setup. It's also got a front end that you can customize
to your own needs. But this is a great example, and I definitely recommend checking it out.
I guess just to set the stage for folks who maybe have heard the term long-running agents but have
maybe not tried to build one or haven't seen one in action, a lot of the agent demos that you see tend
to be stateless. You know, you ask, the model will answer, and then the conversation sort of ends. And even if
the demo lasts like 10 or 15 minutes, it's still living inside a single context window. And you know,
that's going to get filled, and then it'll get discarded. A long-running agent is really the
opposite. It's an agent that maintains its state across sessions, and it operates over a longer
period of time. So we're talking hours, days, maybe even weeks at some point. And your unit of work isn't
really a prompt. It's a workflow. So the agent itself owns a multi-step process end-to-end. And
before I show you a demo, I want to say there are kind of three things that have to be true
for all of this to work. The first is that the agent has to truly be able to sleep. It's a lot like a
person needs to truly be able to sleep. So some of the ideas we might have used before things like
active polling doesn't need that. You don't want that. You don't want to have a blocked thread that
is just sitting there burning compute. And it also has to be able to be dormant until some sort of
external event can wake it up. That might be a web hook, might be a schedule, a human approval,
some sort of human interaction, or a tool callback. The next thing that has to be true
is that every step kind of has to have a checkpoint. That state that we talked about,
a lot of things being stateless, state in this case has to be durably persistent on every transition.
So even if your container running all of this crashes, you still want the server to be able to
redeploy. And a human can then take whatever number of days to complete an action. For example,
if we were going through, you know, employee onboarding, or we were going through a loan
processing setup, however many days it might take for someone to actually complete an action,
the agent needs to be able to still pick up exactly where it left off with no hallucinated memory or
intermediate steps that ever happened. And the third thing that's important is that the agent
can't grade its own work, right? We've seen lots of people use agents where you'll use the same agent to
write your code, and then the same agent to like review your code, right? And I feel like that's,
you need a little bit more nuance to your approach there. Research from a number of labs,
including Anthropic, has been pretty conclusive in terms of like when an agent evaluates its own output,
it consistently overrates it. Like it's almost overconfident about the quality of the outcome.
And so you don't want quality to be mediocre. And the state of the art in this kind of setup is really
having a three agent setup. You want some sort of planner, you want a generator, and you want a
separate evaluator that can test your live results. All right, so here's a visual of what long-running
agents actually look like. And if we put those three ideas together, so durable states, event-driven
dormancy, and separated evaluation, you really stop having a chatbot. You have something that's
able to complete multi-day workflows, multi-week workflows. You know, there's so much in our lives
where we're working with businesses or we're working with other entities, and it just takes a long time
because of the nature of the business to get everything done, to get everything signed, to get
everything analyzed, to get things checked off. And long-running agents are perfect for helping us
compact those workflows, and have agents actually work in the background for us supporting them.
Kind of want to show you the three walls that agents almost often hit. First of all, we have
context degrading, right? So even if you have a long context window, that can fill up pretty quickly,
and it can lead to quality dropping. Every single session can end up starting from zero, and you don't
want that. If you've got a long-running agent, you ideally want to be able to have it continue and
still have context about the problem that you're working on. The next one is that we haven't had so
many primitives for persistent state. And without external structure, you can have agents that drift,
they can break things, or they can just give up because they don't have all of that state, and they
don't understand the full context of the problem. And then we go back to that self-verification that I was
talking about. If a long-running agent can't tell if it's actually done, that's a problem. And if they
praise their own work, even when it's bad, that's also something that we don't want. And so the three
big breakthroughs that have really enabled us to go far here are agent harnesses. Agent harness
engineering, agent harnesses have really gotten better in the last year. And so you're able to have
a harness with agents that can plan, build, evaluate. You don't just have a monolithic loop.
You're able to have persistent memory patterns. So any of those living plans throughout the whole
session can be treated as markdown. You know, you can have change logs as your lab notes. You can have,
you know, people have talked about long-running loops, things like even the Ralph loop. You can have
Ralph loops running in here even, where you're able to just make sure that you're ensuring that the task
gets completed and then manage infrastructure. On the Gemini Enterprise agent platform, just as one
example, we're able to have sessions and memory bank for long-term memory. And that's really the
productized version of this stuff in action.
In this video, we are going to connect an AI agent to an MCP server. You will learn what an MCP server is,
why it matters, and how to connect it to your ADK agent. By the end, your agent won't just write and
plan. It will also pull from an external tool over MCP. So what exactly is MCP?
MCP stands for model context protocol. That sounds complicated, but here's the simple idea.
It's a standard way for agents to talk to external tools. Think of it like a translator. On one side,
you have your agent, which is powered by a language model. And on the other side, you might have tools
that do very specific things like looking up Google trends or querying a database or running code.
The agent itself can't do these things directly. So MCP sits in the middle. So here's how it works.
The tool runs as its own little program, usually in its own process. The agent connects to it over
standard input and output. And then the agent asks, what tools do you have? The MCP server replies with
a list of tool names, their arguments, and what they return. Then the agent says, okay, call this tool
runs and the result comes back as JSON. The important part is how cleanly this is separated.
Each tool runs in its own process, like its own program. The agent doesn't need to know how the
tool is built, what libraries it uses, or even what language it's written in. As long as a tool speaks MCP,
the agent can use it. So why is this so powerful? First off, isolation. If a tool crashes, your agent
doesn't go down with it. Secondly, it's interoperable. You could write tools in Python, Go, or Node,
and the agent doesn't care. Third, it's discoverable. Tools describe themselves in schemas, so agents can
figure out at runtime how to use them. And finally, it's scalable. You can add more tools, swap them out,
or version them without rewriting your entire agent code. So if you think of the agent as the brain,
MCP is the wire that connects it to its hands and eyes in the real world. The brain decides what to
do. MCP carries the request across and the hands do the work. The results come back to the brain.
That's a loop that makes agents more than just chatbots. In the last video, we built an agent that
writes blog posts. You gave it a topic and it planned out the entire sections, wrote a draft,
and even suggested alternative titles. If you haven't seen that yet, check out the first video
or grab the link from the repository linked in the description box below. Now that agent is great,
but right now it only relies on the model. It doesn't know what's happening in the real world,
what is trending, and what is in the news. So in this video, we are going to connect it to an MCP
server that pulls live data from Google Trends. That way our blog writing agent can ground its posts
in what's actually trending right now. Let's open the project directory and create a server.py file.
We are going to look at one python file that does one job. It exposes a single tool called trends over
mcp so our agent can call it in order to see what is trending on Google Trends. Think of this file as
a tiny web service, but instead of http, it talks over standard input and output using the model context
protocol. Let's zoom in on four pieces of code that make this mcp server work with our adk agent. First,
we wrap our plain python function trends as an adk tool. This line is doing a lot for us. We wrote a normal
python function that takes json friendly arguments and returns a json friendly dictionary. Function tool
inspects that function's signature and doc string and it builds a schema and gives the tool a name.
From this point on, adk knows what arguments the tool expects and what it returns. So there's no manual
schema writing which is needed. Next, we create the mcp server object. Think of this as the tiny program that
sits between the agent and our tool. It speaks the model context protocol over a standard input and
output. The name is just an identifier the client will see during the handshake. Now the two handlers
that matter, which is listing tools and calling a tool. So listing tools is how the agent discovers what
this server can do. And when the agent connects to it, it asks, what tools do you have? We answer with a list
containing one item, which is the trends tool. Convert it into an mcp tool schema. And then the helper adk to mcp
tool type function takes the adk function tool metadata and turns it into exactly what the mcp client
expects. That means the agent can see the tool's names, its parameters, their types, and a description.
Everything it needs to construct a valid call at runtime. The agent sends a tool name and a json
dictionary of arguments. We sanity check the name and then forward those arguments straight into our
python function by calling run underscore async on the function tool. Whatever the function returns, we
json dump it and then send it back as a text content payload. If anything goes wrong, we return a small
json error and log the details to standard error. The important idea here is that the protocol is really
simple. Name plus arguments in and json results out. Finally, we attach the server to standard input and
output and run the handshake. This function opens the standard input output transport and hands the read and
write streams to the mcp server. Initialization options contain metadata and the capabilities that the
client will see. In the main block, we call async io.run, which starts the server process. From there,
adk can launch this script, ask for the tools, and call trends like any other tool. Finally, in the main
agent.py file, we just add trends underscore mcp to the root agent's list of tools, right next to the
planner and the writer. From the agent's perspective, there's no difference. Calling trends looks exactly
like calling a local function tool. But now, instead of making something up, the agent can fetch real
trending queries before it starts writing a blog post. Now let's open up adk web ui with this command
and interact with our agent that is now connected to the mcp server. And that's how you connect with your
AI agent to an mcp server. We started with the blog writing agent from the last video,
then added a new server that exposes a trend tool. By wiring that into our root agent, we gave it the
ability to pull in live google trends data before it even started writing. This pattern is powerful
because it keeps your agent lightweight while letting it reach out to the real world through external tools.
thank you for watching and you can check out the description box below for all the resources and
code mentioned in this video. Check out the next video to learn how to build multi-agent systems with adk.
If you've ever built an app that talks to an AI model, MCP changes everything because the way AI
connects to your tools, data, and systems is being completely rewritten. For years, APIs used to be
the glue that held everything together. But now there's a new standard rising fast and that something is
called the model context protocol or MCP. And it might just be the biggest shift since APIs themselves.
So what exactly is MCP and why are people saying it could replace the way we integrate AI with
everything around it? Let's break it down clearly so that by the end of this video you'll understand how
MCP actually works and how it's different from APIs and why it's reshaping how we build agents and
applications that use large language models. For decades, API were the universal handshake between
systems. You define an endpoint, you sent a request, and you got a response back. It's clean and
predictable. And for traditional software, that is perfect. But when large language models enter the
picture, everything changed. Models don't just call one endpoint. They might talk to 10 endpoints,
they want to chain them together, or even interpret unstructured data, and also ask follow-up questions.
And that means they don't just need access to a tool, they also need context. But here's the problem.
APIs are built for programs talking to programs. They are not built for models reasoning over messy
real-world data. An API is like a locked cabinet. You need to know exactly what drawer to open and what
shape the key is. But a model is trying to understand what's inside the cabinet without clear labels. So it
doesn't know which function to call or which parameters to pass until you tell it. And you
have to hard code it sometimes. And oftentimes you have to keep explaining over and over again.
That's where MCP comes in. It was designed to make models autonomously discover and use tools
without the constant hand-holding that we've been doing in prompt engineering.
So before we dive deeper, let's define both sides clearly. APIs are the traditional way
software communicates. They expose specific endpoints, they accept requests in structured
formats like JSON, and they return predictable outputs. Developers document them, secure them,
and version them. But they assume one thing, that both sides knows exactly what to expect. MCP flips
that assumption. Instead of the model needing to be manually thought about each endpoint, MCP gives
the model a standardized way to discover what a tool can do, what kind of inputs it expects, and what kind
of outputs it returns. All through context. Think of it like giving a model a live machine-readable map of
your API instead of a static instruction manual. Now that sounds abstract, so let's make it real. Imagine you're
building an AI agent that manages support tickets. You give it access to Gmail, Notion, and Jira. With APIs,
you'd write custom code for each integration, handle issues like pagination, auth tokens, error cases,
rate limits, and also teach the model through long prompts, like when you want to create a Jira ticket,
call this endpoint with these fields. When you want to reply to an email, call Gmail with this payload.
But with MCP, you don't need to do any of that. Each service, like Gmail, Notion, Jira, exposes an MCP
compatible interface. The model discovers these tools automatically and understands their functions
as part of its environment. You don't tell it how to do it, you give it the context and it figures it
out dynamically. That's the core difference between APIs, which are code level contracts between two
applications and MCP, which is a semantic protocol between a model and its environment. So you're no
longer teaching the model which endpoint to hit, but you're giving it a structured description of what's
available and letting it reason about which tool to use and when. It's like giving the model a toolbox
instead of forcing it to memorize how each tool works. This shift might sound small, but it's
actually massive for developers building agentic systems. With APIs, the logic of what to call and
when to call it lived in your app code. With MCP, that logic can actually move into the model's reasoning
layer itself. You can now build a general purpose agent that can plug into any tool that supports the
protocol without having to rewrite code for each integration. That's the magic here and it's
standardization. The same way HTTP made websites interoperable, allowing them to share and use data with
each other and other systems and letting them work together to perform tasks with minimal human intervention.
MCP is trying to make AI environments interoperable. But let's talk about what's actually happening under the hood.
An MCP server is a lightweight process that sits next to your service or data source. It describes what it can do and
what functions it exposes all using JSON schemas. The model connects to this server through a standardized interface like WebSocket or
HTTP and receives metadata about the available resources. Once connected, the model can call
these functions directly, not by guessing, but by using the metadata. It knows what inputs are required and
what each field means and what type of output to expect. The beauty is that everything is self-describing. You don't
have to prompt engineer the schema or reformat responses. It's all standardized. Compare that to an API
where every single integration is bespoke. You need a developer to read the docs, map the payloads and
manually wrap the endpoints. So MCP abstracts that away. This means instead of building 100 custom integrations,
you build one MCP interface and every compatible model can use it instantly. That's why people are
calling MCP the plug and play layer for AI systems. Now, this doesn't mean APIs are going away. APIs are
still the foundation. They're how your systems actually function. But MCP changes how models access those
APIs. Think of it like this. MCP doesn't replace your backend. It replaces the middleware between the model
and the API. The MCP server acts like a translator, converting your existing APIs into a format that
models can understand automatically. So instead of saying MCP versus API, it's more like MCP on top of APIs.
This distinction is key. MCP doesn't compete with APIs. It actually leverages them. But it changes who
the client is. With API, the client is another program or user. With MCP, the client is the model itself.
And that subtle difference changes everything about how we design integrations. Let's zoom out for a bit.
The rise of MCP is part of a bigger movement towards model-native software architecture. For decades,
we've built systems for humans and for code. Now we're building systems for models. And models
don't consume REST endpoints the way code does. They consume context, which includes structure
descriptions, schemas, and examples. They do this so that they can reason, plan, and act. So MCP gives them
that in a standardized way. That's why developers building agent frameworks are moving in this
direction. They're realizing that connecting a model to a world of tools isn't about a bigger context
window. It's about cleaner protocols. And let's be honest, it's not all magic. MCP is still pretty new.
The biggest challenge right now is adoption. For MCP to truly work, the ecosystem needs servers, clients,
and tools to agree on the same standard. Another huge challenge is security and control. When models
can directly call tools through a protocol, you need clear permission layers. You don't want a model
accidentally sending an email, deleting a file, or making a huge database change that it wasn't
supposed to. APIs handle that through authentication, keys, and rate limits. MCP needs to bring those guardrails
into its protocol layer, which is already happening. The spec defines capabilities, scopes, and authentication
methods that keep things safe. But it's still early days. And the final challenge is the developer mindset.
Most of us grew up in an API world. We think in terms of endpoints and routes. MCP asks us to think in
terms of capabilities and context to design systems that describe what they can do, not just how to do
it. That's a huge paradigm shift, but it's worth learning early. Here's where it all comes together.
Think about the moment when HTTP unified the internet. Before that, every service had its own protocol,
from FTP, Gopher, Telnet, which are all different internet protocols. Once the web standardized on
HTTP, suddenly everything became interoperable. MCP is doing the same thing for AI agents. Instead of
each company inventing its own plugin format or integration layer, MCP provides a single open
protocol that any model can understand. You build your connector once and any compliant model can use it.
That means the future of AI tools will look less like custom integrations and more like a shared
ecosystem. You will have an MCP server for your product and any AI like Gemini, Claude, GPT can use
it instantly. That's the world we're heading towards. One where models, not just humans, become first class
users of software. So to sum it all up, APIs are not dead. They are just evolving. APIs were made for
deterministic systems. One program asking another for data. And MCP is made for probabilistic systems,
a model reasoning about what it can do. So the next time someone says MCP versus API, just remember it's
not a direct comparison. It's a foundation being rebuilt. MCP sits one layer above APIs and turning
them from static routes into living interfaces that models can actually reason about. And as more
frameworks adopt it, you'll start seeing a new pattern emerge. Instead of hard-coded integrations,
we'll build model-aware systems where context tools and reasoning can all live in harmony. I hope this video
was helpful in explaining the differences between MCPs and APIs. To learn more about the model context
protocol at a deeper level, check out this next video.
Hey everyone, in this video, you're going to learn how to get started with ADK. That's Agent Development Kit.
This is a framework from Google to make it really easy for you to build agents that can work together.
First, let's talk about what is an agent. An agent is an LLM with tools running in a loop to complete a
task. ADK is going to give you a framework, so a lot of that boilerplate code that you can avoid writing,
that will help you equip an LLM with tools and then help you handle the control of it running in a loop
and deciding when it needs to stop working on a task, etc. You also get some really nice interfaces for
testing out your agents during the development process. So first, we're going to walk through
how to get to Hello World with ADK, how to build your first agent, how to equip that agent with some
tools, and then we're going to look at building a very simple multi-agent system. Before we get
started though, there's a couple pieces of setup you're going to need to do. You're going to want to
go to AI Studio to generate an API key to interact with the Gemini API. You're also going to want to
pip install Google ADK and I recommend doing all of this within a virtual environment. But once you
have an API key and once you have the ADK Python package installed, then we can get started. To
create your first agent, once you have ADK installed, you're just going to do ADK create first underscore
agent. Cool. All right, once you've created your first agent, you can choose what model you want
to use with it. And so we will do here Gemini 3 flash preview. And you can see that the code to create
your first agent is pretty minimal. We're really just importing the Google ADK agents library and then
we define an agent just passing in a few parameters. So it's the model that we're going to use. That's the
name for the agent. We'll just call this one getting started. And then a description of that agent and
then instructions. This is also known as the system message or the system prompt. For this case, let's just
say you are an assistant who is helpful, but brief. All right. And that's it. That's all you need to write in
order to create your first agent. Now, one thing I really like about ADK is that it makes it very simple to
test your agents. So I'm going to switch over the terminal here and I'm going to type ADK run first agent. All right,
then to test our agent, we're just going to run ADK run first agent. And we have this dialog here.
And we can just say, hello, how are you today? And we'll get a reply back from our agent. So this is
the way that we can test our agents built in ADK right here locally. ADK comes with another really
nice feature, which is a web interface to test these as well. So I can also type ADK web and you see that
it will spin up a web server here. And then there is a URL, a 1-2-7-0-0-1-8000. And if I go and open that up in a browser,
you can see that I have access here to my first agent. I can also type hello. How are you today here? And I can get responses from my agent.
And then I also can see the stack trace. And so this web interface is really, really helpful when you're building agents for
debugging purposes. All right. So that's how we get started with ADK and how we build our first agent.
But right now, all we're really doing is having a conversation with an LLM. And that LLM is a little bit limited in what it knows and what it can do.
Of course, it's been trained on an enormous amount of data. It's very powerful. But that data has a cutoff date.
And so if you were to ask the model, for instance, what time is it or what is today's date?
If it gave you an answer, it probably would not be correct. The correct answer is it doesn't know,
right? Because LLMs do not know up to the date information. But we can equip LLMs with tools so
that they can retrieve up to the date information or so that they can perform tasks. So let's look at
equipping our agent with its first tool. I'm going to create a new agent here called Timekeeper.
Very similar structure. The only difference from our initial agent is that we are going to add a
function at the top of this file called get current time. That get current time Python function does a
very simple thing. It returns the current date time. Then the second change that we will make to our file
is that we are going to add a line called tools. And that tools has a list. And the list here only
includes a single function, and that is get current time. So we basically have defined a tool here in
get current time. And then we have equipped the agent with this tool. And note, because this is a list,
we could equip it with multiple tools. But here we're just giving it a single tool. So now if I go
back to my command line, and I run ADK again, and I test out this agent, this agent will have access
to the current time and date. It's called Timekeeper.
And great. And so now when we run what time is it, it says it's currently 1.30pm on April 2. And I
can confirm that is the date and time that we are recording this currently. So what we've done here
is we've given the agent access to a tool so that it can get information that the LLM would not have
had available to it before. This is a really, really powerful concept because this allows us to extend
the abilities of the large language model almost infinitely. Let's look at adding another tool to it. And
this one will be Google search. So this is another agent. This one looks very similar to the Timekeeper
agent that we just created. The difference here is that we are not defining the tool here in the code.
Instead, we are just importing the Google search tool. This is a tool that is baked into ADK. So you
get it for free with this framework. And then we add down here to the tools, Google search tool,
and we are telling it to bypass multiple tools limit. By default, there is a restriction that only allows
it to do a single tool call. But Google search often needs to do multiple tool calls in order to
give you comprehensive results. So we're going to set bypass multiple tools limit to true and give
this agent access to the Google search tool. And now if we come over here to ADK and we do ADK run
search agent, we're going to say here, uh,
uh, when does the next episode, uh, all right. So now when I ask my agent, when does the next episode
of top chef air and what's happened so far this season, the first thing you're going to notice is
that we get a much longer delay between my query and the response. Uh, but then we do get, uh,
a longer response back. Let's also take a look at what it's doing in the web console. So I'm going
to go into the web interface here and I'm going to ask my search agent, when does the next episode
of top chef air and what has happened so far in this season. Now you can see that it takes
a little while for me to get a response back. Uh, but that's because it is going out and it's
searching Google to collect this information. And if we want to click on our search agent here,
you can see on the left-hand side that it's going to show all of the sources that the Google search
tool searched for in order to gather this information and to compile the results. Over in
our summary, we have our recap and our recap even gave us the sources back. Uh, there might be one
problem though. Some of these sources are going to 404. So this is not perfect. And we did actually
search and, uh, search real sources to compile this information, but LLMs still sometimes hallucinate,
uh, URLs. And so what I want to do is build a multi-agent system that will confirm the data
that is being reported back by this search agent, right? So we're going to verify the URLs that are,
that come back. So let's move on to the third part and that's building multi-agent systems.
All right, to build our multi-agent system, we're first going to create another agent. And this one
is going to be called URL Verifier. Our URL Verifier agent is a little bit more complex
than what we've seen so far, but the main thing to keep in mind here is that we are equipping it
with a tool called Fetch URL. And we're going to pass a URL to this Fetch URL and it's going to return
the, uh, text that is located on that webpage. Then we're going to set up an agent that is going to
take in the information from that URL. It is equipped with that Fetch URL tool, and it is going to
return verified, not verified, or inconclusive. So we basically have built here what some might
call LLM as a judge. So we're passing in information from one large language model request to another,
and we're giving that other one the tools to verify if that information was accurate or not.
We're going to set up a second agent. Uh, this one is going to be called our researcher agent.
So our researcher agent now has two tools, but those tools are agents, right? So this is where
things can start to get really powerful when you are equipping agents, not just with tools that are
deterministic functions that run, but when you are equipping agents with other agents as tools. So
in this case, our researcher agent is going to serve as our orchestrator, and we are equipping it with the
search agent and the verify agent as tools that it can use in its process to verify this information.
We change up the instructions a little bit. We tell it that it is a research assistant,
that it needs to use the search agent tool to find information, and then it's going to use the
verifier in order to confirm the information is accurate. And so now if we come over to our web
interface and we ask, when does the next episode of Top Chef Air, we can see that it is making
multiple tool calls in order to get this information for us. So it is using first the search agent,
and then it uses the URL verifier in order to pull up the information on that URL and confirm
if the information that the initial search agent had retrieved was actually correct. And to confirm that
that URL actually does exist. So in this way, by combining multiple tools together and by equipping
an orchestrator agent with multiple other agents that only have a single purpose, we're able to
overcome some of the limitations of large language models. In this way, you're able to give each large
language model or each agent a very specific task, and you can have better management of its performance,
of its memory, of its cost. We could also have each agent being powered by a different
large language model. So for instance, for simpler tasks, we could use a cheaper and faster model.
For more complex tasks that required more reasoning, we could use more expensive,
but more advanced models. So these multi-agent systems give you much, much, much more control
over the types of tasks that you can accomplish, and with what certainty you can accomplish them,
and then with what cost it requires in order to accomplish them, then you can get by just building
one agent that has a whole bunch of different tools. If you'd like to get started on this,
just visit adk.dev and walk through the get started.
