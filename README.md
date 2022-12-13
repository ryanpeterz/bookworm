# BookWorm
There's no substitute for doing the reading.

## How to Install
### [Sign up](https://beta.openai.com/signup) for an openai account
*Read the ToS for yourself*. You'll be prompted to create an organization. *Name it something cool.*
### [Find your Organization ID](https://beta.openai.com/account/org-settings)
*It's the greyed out garbage text that looks like `org-AW123joia&ADFGAQ#$`.*

### [Add an API key](https://beta.openai.com/account/api-keys)
*More random garbage, this time like `sk-130B4985eorfg325r4q`.* **Write this down somewhere ephemeral.**

### Open a terminal and run these commands
*You may want to create a conda environment first.*
```bash
.../bookworm$ pip install -r requirements.txt
.../bookworm$ python3
>>> import keyring
>>> keyring.set_password("bookworm", "org", <your-organization-id>)
>>> keyring.set_password("bookworm", "key", <your-secret-api-key>)
```

## How to Run
*Presently (persnicketily, finickily):*
```bash
.../bookworm$ python3 main.py "Rights of Man"
```
*Eventually...*
```bash
(know) user@machine:~$ python -m bookworm.read path/to/source
```

## Cost to Run
The cost [depends](https://openai.com/api/pricing/) on how much BookWorm reads.

*For Answer to Burke, it's ~2 USD*

## What it Does
> What does a BookWorm do?

ChatGPT:
> A bookworm is someone who loves to read books. They are often considered to be very knowledgeable and well-read, as they spend a lot of their time reading. Some bookworms may have a particular interest in a specific genre or type of literature, while others may enjoy reading a wide variety of books. Ultimately, a bookworm is someone who is passionate about reading and learning new things through the written word.

After reading "Rights of Man: Being an Answer to Mr. Burke's Attack on the French Revolution", BookWorm produced this summary based on a prompt that *did not mention the text by title*.

> The French Revolution sought to free its people from oppressive government and grant fundamental rights to all citizens, providing a blueprint for future generations of how to create a government based on wisdom and reason, giving individuals the rights and freedoms they deserve. Mr. Burke's attack on the Revolution is an attempt to mischaracterize its motives and accomplishments, but the legacy of the Revolution should not be forgotten. Its model of establishing universal rights and freedoms, abolishing titles and hierarchies, and creating the paths of equality and justice has been a model for freedom and progress worldwide. People of all ages have the right to govern their own affairs, and governments must reflect the wisdom and reason of the people rather than the oppressions of the past.
