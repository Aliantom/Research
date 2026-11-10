<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Transcript: Mastering Claude Code in 30 minutes

> **TL;DR:** Transcript of Boris Cherny's talk Mastering Claude Code in 30 minutes (Anthropic, uploaded 2025-05-22): Whisper turbo, with the mis-heard product name corrected by regex.
> **Source:** https://x.com/chesny/status/2116539147540197436 (repost of https://www.youtube.com/watch?v=6eBSHbLKuN0)  ·  **Updated:** 2026-11-02

Whisper turbo, generated 2026-11-02. "QuadCode", "QuadMD" and similar were replaced by regex, so other small errors remain. Check quotes against the audio. Timed versions: `~/Videos/YouTube/x-chesny-2116539147540197436/` (`.srt`, `.vtt`).

Hello.
Hey everyone.
I'm Boris.
I'm a member of technical staff here at Anthropic and I created Claude Code.
And here to talk to you a little bit about some practical tips and tricks for using Claude Code.
It's going to be very practical.
I'm not going to go too much into the history or the theory or anything like this.
And yeah, before we start, actually, can we get a quick show of hands?
Who has used Claude Code before?
Yeah.
All right.
That's what we like to see.
For everyone that didn't raise your hands, I know you're not supposed to do this while people are talking, but if you can open your laptop and type this, and this will help you install Claude Code just so you can follow along for the rest of the talk.
All you need is Node.js if you have it.
This should work.
If you want us all to open the Claude Code.
Yeah.
Well, you don't have to follow along, but if you don't have it yet, yeah, this is your chance to install it so you can follow along.
So what is Claude Code?
Claude Code is a new kind of AI assistant.
And there's been different generations of AI assistants for coding.
Most of them have been about completing, you know, like a line at a time, completing a few lines of code at a time.
Claude Code is not for that.
It's fully agentic.
So it's meant for building features, for writing entire functions, entire files, fixing entire bugs at the same time.
And what's kind of cool about Claude Code is it works with all of your tools.
And you don't have to change out your workflow.
You don't have to swap everything to start using it.
So whatever IDE you use, if you use VS Code or if you use Xcode or if you use JetBrains IDEs, there's some people at Anthropic that you can't pry them from their cold, dead hands, but they use Claude Code because Claude Code works with every single IDE, every terminal out there.
It'll work locally over remote SSH, over Tmux, whatever environment you're in, you can run it.
It's general purpose.
And this is something where if you haven't used these kind of free form coding assistants in the past, it can be kind of hard to figure out how to get started because you open it up and you just see a prompt bar and you might wonder, like, what do I do with this?
What do I type in?
It's a power tool, so you can use it for a lot of things.
But also, because it can do so much, we don't try to guide you towards a particular workflow.
Because really, you should be able to use it however you want as an engineer.
As you open up Claude Code for the first time, there's a few things that we recommend doing to get your environment set up.
And these are pretty straightforward.
So run terminal setup, this will give you shift enter for new lines, so you don't have to do like backslashes to enter new lines.
This is, you know, it makes it a little bit nicer to use.
Do slash theme to set light mode or dark mode or Daltonize themes.
You can do slash install GitHub app.
So today we announced a GitHub app where you can add mention Claude on any GitHub issue or pull request.
So to install it, just run this command in your terminal.
You can customize the set of allowed tools that you can use so you're not prompted for it every time.
This is pretty convenient.
For stuff that I'm prompted about a bunch, I'll definitely customize it in this way so I don't have to accept it every time.
And something that I actually do is for a lot of my prompts, I won't hand type them into Claude Code.
If you're on macOS, you can go into your system settings under accessibility as dictation and you can enable it.
And so something I do is you just hit like that dictation key twice and you can just speak your prompt.
And it helps a lot to have specific prompts.
So this is actually pretty awesome.
You can just talk to Claude Code like you would another engineer and you don't have to type a lot of code.
So when you're starting out with Claude Code, it's so freeform and it can do everything.
What do you start with?
The thing I recommend above everything else is starting with codebase Q&A.
So just asking questions to your codebase.
This is something that we teach new hires at Anthropic.
So on the first day in technical onboarding, you learn about Claude Code, you download it, you get it set up, and then you immediately start asking questions about the codebase.
And in the past when you're doing technical onboarding, it's something that taxes the team a lot, right?
You have to ask other engineers on the team questions, you have to look around the code and this takes a while, you have to figure out how to use the tools, this takes a long time.
With Claude Code, you can just ask Claude Code and it'll explore the codebase, it'll answer these kind of questions.
And so at Anthropic, onboarding used to take about two or three weeks for technical hires.
It's now about two or three days.
What's also kind of cool about Q&A is we don't do any sort of indexing.
So there's no remote database with your code, we don't upload it anywhere, your code stays local, we do not train generative models on the code.
So it's there, you control it, there's no indices or anything like this.
And what that means is also there's no setup.
So you start Claude, you download it, you start it, there's no indexing, you don't have to wait, you can just use it right away.
This is a technical talk, so I'm going to show some very specific prompts and very specific code samples that you can use and hopefully improve and up level your Claude Code experience.
So some kind of questions that you can ask is, you know, like how is this particular piece of code used or how do I instantiate this thing?
And Claude Code, it won't just do like a text search and try to answer this, it'll often go a level deeper and it'll try to find examples of how is this class instantiated?
How is it used?
And it'll give you a much deeper answer, so something that you would get out of a wiki or documentation, instead of just like command F.
Something that I do a lot also is ask it about git history.
So for example, you know, why does this function have 15 arguments and why are the arguments named this weird way?
And this is something I bet in all of our code bases you have some function like this or some class like this.
And Claude Code can look through git history and it'll look to figure out how did these arguments get introduced and who introduced them and what was the situation?
What are the issues that those commits link to?
And it'll look through all this and summarize it.
And you don't have to tell it that in all this detail, you just ask it.
So just say look through git history and it'll know to do this.
The reason it knows, by the way, is not because we prompted it to.
There's nothing in the system prompt about looking through git history.
It knows it because the model is awesome.
And if you tell it to use git, it'll know how to use git.
So we're lucky to be building on such a good model.
I often ask about GitHub issues.
So, you know, I can use WebFetch and I can fetch issues and look up context on issues too, and this is pretty awesome.
And this is something that I do every single Monday in our weekly standup is I ask what did I ship this week?
And Claude Code looks to the log, it knows my username, and it'll just give me a nice readout of everything I shipped.
And I'll just copy and paste that into a document.
So yeah, that's tip number one.
For people that have not used Claude Code before, if you're just showing it to someone for the first time, onboarding your team, the thing we definitely recommend is start with code-based Q&A.
Don't start by using fancy tools, don't start by editing code, just start by asking questions about the code base.
And that'll teach people how to prompt.
And it'll start teaching them this boundary of like, what can Claude Code do?
What is it capable of versus what do you need to hold its hand with a little bit more?
What can be one-shotted, what can be two-shotted, three-shotted?
What do you need to use interactive mode for in a REPL?
Once you're pretty comfortable with Q&A, you can dive into editing code.
This is the next thing.
And the cool thing about any sort of agentic, you know, like using an LM in an agentic way is you give it tools and it's just like magical.
It figures out how to use the tools.
And with Claude Code, we give it a pretty small set of tools.
It's not a lot.
And so it has a tool to edit files.
It has a tool to run bash commands.
It has a tool to search files.
And it'll string these together to explore the code, brainstorm, and then finally make edits.
And you don't have to prompt it specifically to use this tool and this tool and this tool.
You just say, you know, do this thing and it'll figure out how to do it.
It'll string it together in the right way that makes sense for Claude Code.
There's a lot of ways to use this.
Something I like to do sometimes is before having Claude jump in to write code, I'll ask it to brainstorm a little bit or make a plan.
This is something we highly recommend.
And something I see sometimes is people, you know, they take Claude Code and they ask it, hey, implement this enormous like 3,000 line feature.
And sometimes it gets this right on the first shot.
But sometimes what happens is the thing that it builds is not at all the thing that you wanted.
And the easiest way to get the result you want is ask it to think first.
So brainstorm ideas, make a plan, run it by me, ask for approval before you write code.
And you don't have to use plan mode, you don't have to use any special tools to do this.
All you have to do is ask Claude.
And it'll know to do this.
So just say, before you write code, make a plan.
That's it.
This is also, I want to think with this one, this commit push PR, this is a really common incantation that I use.
There's nothing special about it.
But Claude is kind of smart enough to interpret this.
So it'll make a commit, it'll push it to the branch, make a branch, and then make a pull request for me on GitHub.
You don't have to explain anything.
It'll look through the code, it'll look through the history, it'll look through the Git log by itself to figure out the commit format and all the stuff.
And it'll make the commit and push it the right way.
Again, we're not system prompting it to do this.
It just knows how to do this.
The model is good.
As you get a little bit more advanced, you're going to want to start to plug in your team's tools.
And this is where Claude Code starts to really shine.
And there's generally two kinds of tools.
So one is bash tools.
And an example of this, I just made up this like barley CLI, this isn't a real thing.
But you can say use the CLI to do something.
And you can tell Claude Code about this.
And you can tell it to use, for example, like dash dash help to figure out how to use it.
And this is efficient.
If you find yourself using it a lot, you can also dump this into your CLAUDE.md, which we'll talk about in a bit, so Claude can remember this across sessions.
But this is a common pattern we follow at Anthropic, and we see external customers use too.
And same thing with MCP.
Claude Code can use bash tools, it can use MCP tools.
So, you know, just tell it about the tools.
And you can add the MCP tool, and you can tell it how to use it, and it'll just start using it.
And this is extremely powerful, because when you start to use code on a new code base, you can just give it all of your tools, all the tools your team already uses for this code base.
And Claude Code can use it on your behalf.
There's a few common workflows.
And this is the one that I talked about already, so kind of do a little bit of exploration, do a little bit of planning, and ask me for confirmation before you start to write code.
These other two on the right are extremely powerful.
When Claude has some way to check its work, so for example by writing unit tests, or screenshotting in Puppeteer, or screenshotting the iOS simulator, then it can iterate.
And this is incredible, because if you give it, for example, a mock, and you say build this web UI, it'll get it pretty good.
But if you had to iterate two or three times, often it gets it almost perfect.
So the trick is give it some sort of tool that it can use for feedback to check its work, and then based on that it will iterate by itself, and you're going to get a much better result.
So whatever your domain is, if it's unit tests, or integration tests, or screenshots for apps, or web, or anything, just give it a way to see its result, and it'll iterate and get better.
So these are the next steps.
Teach Claude how to use your tools and figure out the right workflow.
If you want Claude to jump into code, if you want it to brainstorm a little bit, make a plan, if you want it to iterate, kind of have some sense of that, so you know how to prompt Claude to do what you want.
As you go deeper, beyond tools, you want to start to give Claude more context.
And the more context, the smarter the decisions will be, because as an engineer working in a codebase, you have a ton of context in your head about your systems, and all the history, and everything else.
So there's different ways to give this to Claude.
And as you give Claude more context, it'll do better.
There's different ways to do this.
The simplest one is what we call CLAUDE.md.
And CLAUDE.md is the special file name.
The simplest place to put it is in the project root.
So the same directory you start Claude in, put a CLAUDE.md in there.
And that'll get automatically read into context at the start of every session.
And essentially, the first user turn will include the CLAUDE.md.
You can also have a local CLAUDE.md.
And this one, you don't usually check into source control.
So CLAUDE.md, you should check into source control, share with your team so that you can write it once and share it with your team.
This one, you don't check in.
It's just for you.
The kinds of things you put in CLAUDE.md, it's like common bash commands, common MCP tools, architectural decisions, important files, anything that you would kind of typically need to know in order to work in this codebase.
Try to keep it pretty short, because if it gets too long, it's just going to use up a bunch of context.
And it's usually not that useful.
So just try to keep it as short as you can.
And for example, in our codebase, we have common bash commands, we have a style guide, we have a few core files, kind of things like that.
All the other CLAUDE.md files, you can put them in other nested child directories, and Claude will pull them in on-demand.
So these are the CLAUDE.md files that will get pulled in automatically.
But then also you can put CLAUDE.md files in nested directories, and those will get automatically pulled when Claude works in those directories.
And of course, if you're a company, maybe you want a CLAUDE.md that's shared across all the different codebases, and you want to manage it on behalf of your users, and you can put in your enterprise route, and that will get pulled in automatically.
There's a ton of ways to pull in context.
I actually had a lot of trouble putting this slide together just to communicate the breadth of ways you can do this.
But CLAUDE.md is pulled in automatically.
You can also use slash commands.
So this is .claude slash commands, and this can be in your home directory, or it can be checked into your project.
And this is for slash commands.
And over here, we have a few examples of the slash commands that we have in Claude Code itself.
And so for example, if you're in the Claude Code repo, and you see issues getting labeled, that's actually this workflow running here.
It's labeled GitHub issues.
And we have a GitHub action running, the same one we talked about this morning, where Claude Code will run this command, and it's just a slash command.
It'll run, and it'll label the issues so humans don't have to.
It just saves us a bunch of time.
And of course, you can add mention files to pull them into context.
And like I said before, CLAUDE.md files in a nested directory get pulled in when Claude works in that directory.
So give Claude more context, and it's definitely worth taking the time to tune context.
You can run it through a prompt improver.
Consider who the context is for.
If you want to pull it in every time, if you want to pull it in on demand, if you want to share it with a team, if it's a personal preference, definitely take the time to tune it.
This will improve performance dramatically if you do it right.
As you get more advanced, you're going to want to think about this a little bit more, this kind of hierarchy of different ways to pull in everything.
So like not just CLAUDE.md, but also config and kind of everything about Claude you can pull in in this hierarchical way.
So projects are specific to your Git repo, and this you can check in, or you can make it just for you.
You can also have global configs that are across all your projects, or you can have enterprise policies.
And this is essentially a global config that you roll out for all of your employees, everyone on your team automatically.
And this slide is like pretty information dense, but the point is this applies to a lot of stuff.
So you can do this for slash commands, you can do it for permissions.
So for example, if you have a bash command that you would run for all your employees, like all your employees use this like test command, for example.
You can actually just check it into this enterprise policies file, and then any employee, when they run this command, it will be auto-approved, which is pretty convenient.
And you can also use this to block commands.
So for example, let's say there's a URL that should never be fetched.
Just add it to this config, and that'll make it so an employee cannot override it, and that that URL can never be fetched.
So pretty convenient, both to unblock people and also just to keep your code base safe.
And then same thing for MCP servers.
Have a MCP JSON file, check it into the code base.
That way, any time someone runs Claude code in your code base, they'll be prompted to install the MCP servers, and share it with the team.
If you're not sure which of these to use, this is like a kind of an insane matrix, because we support a lot of stuff, and engineer workflows are very flexible, and every company is different.
So we kind of want to support everything.
So if you're not sure how to get started, I would recommend start with shared project context.
You write this once, and then you share it with everyone on the team, and you get this kind of network effect where, you know, someone does a little bit of work, and everyone on the team benefits.
There's a lot of tools built into Claude to manage this.
So as an example, if you run slash memory, you can see all the different memory files that are getting pulled in.
So maybe I have an enterprise policy, I have my user memory, I have project Claude MD, and then maybe there's a nested Claude MD that's only pulled in for certain directories.
And then similarly, when you do slash memory, you can edit particular memory files.
When you type pound sign to remember something, you can pick which memory you want it to go to.
So yeah, that's the next step.
Take the time to configure Claude MD, MCP servers, all the stuff that your team uses, so that you can use it once, configure it once, and then share it with everyone.
An example of this is in our apps repo for Anthropic.
This is like the repo that we have all of our web and apps code in.
There's a Puppeteer MCP server, and we share this with the team.
And there's an MCP JSON checked in, so any engineer working that repo can use Puppeteer in order to pilot end-to-end tests and to screenshot automatically and iterate so that every engineer doesn't have to install it themselves.
This is a talk about pro tips.
I just want to take a quick interlude to talk about some common key bindings that people may not know.
It's very hard to build for terminal.
It's also very fun.
It feels like rediscovering this new design language.
But something about terminals, it's extremely minimal.
And so sometimes it's hard to discover these key bindings.
And here's just a quick reference sheet.
So anytime, you can hit shift tab to accept edits.
And this switches you into auto accept edits mode.
So bash commands still need approval, but edits are auto accepted.
And you can always ask Claude to undo them later.
For example, I'll do this if I know Claude's on the right track or if it's writing unit tests and iterating on tests.
I'll usually just switch into auto accept mode so I don't have to okay every single edit.
Anytime you want Claude to remember something, so for example, if it's not using a tool correctly and you want it to use it correctly from then on, just type the pound sign and then tell it what to remember.
And it'll remember it.
It'll incorporate it into CLAUDE.md automatically.
If you ever want to drop down to bash mode, so just run a bash command, you can hit the exclamation mark and type in your command.
That'll run locally, but that also goes into the context window.
So Claude will see it on the next turn.
And this is pretty good for long running commands if you know exactly what you want to do or any command that you want to get into context.
And Claude will see the command and the output.
You can add mention files and folders.
Anytime you can hit escape to stop what Claude is doing.
No matter what Claude is doing, you can always safely hit escape.
It's not going to corrupt the session.
It's not going to mess anything up.
So maybe Claude is doing a file edit.
I'll hit escape.
I'll tell it what to do differently.
Or maybe it suggested a 20 line edit and I'm like, actually 19 of these lines look perfect, but one line you should change.
I'll hit escape.
I'll tell it that.
And then I'll tell it to redo that.
You can hit escape twice to jump back in history.
And then after you're done with the session, you can start Claude with a resume to resume that session if you want.
Or dash dash continue.
And then anytime if you want to see more output, hit control R.
And that'll show you the entire output, the same thing that Claude sees in its context window.
The next thing I want to talk about is the Claude code SDK.
So we talked about this at the top.
Right after this, Sid is doing a session, I think, just across the hallway.
And he's going to go super deep on the SDK.
If you hadn't played around with this, if you used the dash P flag in Claude, this is what the SDK is.
And we've been planning a bunch of features over the last few weeks to make it even better.
So yeah, you can build on top of this.
You can do cool stuff.
This is exactly the thing that Claude code uses.
It's exactly the same SDK.
And so, for example, something you can do is Claude dash P.
So this is the CLI SDK.
You can pass a prompt.
You can pass some allowed tools, which could include specific bash commands.
And you can tell it which format you want.
So you might want JSON or you might want streaming JSON if you want to process this somehow.
So this is awesome for building on.
We use this in CI all the time.
We use this for incident response.
We use this in all sorts of pipelines.
So really convenient.
Just think of it as like a Unix utility.
You give it a prompt.
It gives you JSON.
You can use this in any way.
You can pipe into it.
You can pipe out of it.
The piping is also pretty cool.
So you can use, for example, git status and pipe this in and use JQ to select the result.
The combinations are endless.
And it's sort of this new idea.
It's like a super intelligent Unix utility.
And I think we barely scratched the surface of how to use this.
We're just figuring this out.
You can read from like a GCP bucket.
Read, you know, like a giant log and pipe it in and tell Claude to figure out what's interesting about this log.
You can fetch data from like the Sentry CLI.
You can also pipe it in and have Claude do something with it.
The final thing, and this is probably like the most advanced use cases we see.
I'm sort of a Claude normie.
So I'll have usually like one Claude running at a time.
And maybe I'll have like a few terminal tabs for a few different repos running at a time.
When I look at power users in and out of Anthropic, almost always they're going to have like SSH sessions.
They'll have like Tmux tunnels into their Claude sessions.
They're going to have a bunch of checkouts of the same repo so that they can run a bunch of Claude's in parallel in that repo.
Or they're using Git work trees to have some kind of isolation as they do this.
And we're actively working on making this easier to use.
But for now, like these are some ideas for how to do more work in parallel with Claude.
You can run as many sessions as you want.
And there's a lot that you can get done in parallel.
So yeah, that's it.
I wanted to also leave some time for Q&A.
So I think this is the last slide that I have.
And yeah, if folks have questions, there's mics on both sides.
And yeah, we'd love to answer any questions.
I did.
Hey, Boris.
Thanks for building a Claude Code.
And I was wondering what was the hardest implementation, like part of the implementation for you of building it?
I think there's a lot of tricky parts.
I think one part that is especially tricky is the things that we do to make bash commands safe.
Bash is inherently pretty dangerous and it can change system state in unexpected ways.
But at the same time, if you have to manually approve every single bash command, it's super annoying as an engineer.
And you can't really be productive because you're just constantly approving every command.
And just kind of navigating how to do this safely in a way that scales across the different kinds of code bases people have, because not everyone runs their code in a Docker container, was pretty tricky.
And essentially, the thing we landed on is there's some commands that are read-only.
There's some static analysis that we do in order to figure out which commands can be combined in safe ways.
And then we have this pretty complex tiered permission system so that you can allow list and block list commands at different levels.
Hi, Boris.
You mentioned giving an image to Claude Code, which made me wonder if there's some sort of multimodal functionality that I'm not aware of.
Are you just pointing it at an image on the file system or something?
Yeah, so Claude Code is fully multimodal.
It has been from the start.
It's in a terminal, so it's a little hard to discover.
But yeah, you can take an image and just drag and drop it in.
That'll work.
You can give it a file path that'll work.
You can copy and paste the image in, and that works too.
So I'll use this pretty often for if I have like a mock of something, I'll just drag and drop in the mock.
I'll tell it to implement it.
I'll give it up a tier server so it can iterate against it.
And yeah, it's just fully automated.
Hey, why did you build a CLI tool instead of an IDE?
Yeah, it's a good question.
I think there's probably two reasons.
One is we started this at Anthropic.
And at Anthropic, people use a broad range of IDEs.
And some people use VS Code.
Other people use Zed or Xcode or Vim or Emacs.
And it was just hard to build something that works for everyone.
And so terminal is just the common denominator.
The second thing is at Anthropic, we see up close how fast the model is getting better.
And so I think there's a good chance that by the end of the year, people aren't using IDEs anymore.
And so we want to get ready for this future.
And we want to avoid over-investing in UI and other layers on top, given that the way the models are progressing, it just, it may not be useful work pretty soon.
Yeah.
How much have you, I don't know if this is, is this on?
How much have you used Claude Code for machine learning modeling and almost that AutoML experience?
I was curious what the experience has been so far with that.
Yeah, I think the question was, how much are we using Claude Code for machine learning and modeling?
We actually use it for this a bunch.
So both engineers and researchers at Anthropic use Claude Code every day.
I think about 80% of people at Anthropic that are technical use Claude Code every day.
And hopefully you can see that in the product and kind of the amount of love and dog fooding we've put into it.
But this includes researchers who use tools like the notebook, notebook tool to edit and run notebooks.
Okay, very cool.
Thank you.
All right.
I think that's it.
Thanks.
All right.
Thank you. 
