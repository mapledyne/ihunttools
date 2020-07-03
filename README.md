# ihunttools

A basic command line app to generate #iHunt job cards that look like a phone screenshot.

## Installation

Copy or clone this directory and run the command (exmaples below). Working on a better front end that can be web accessible, but it's just command line for the time being.

You'll need to have Pillow installed:

`pip install -r requirements.txt`

## Examples

A very simple usage of this consists of a few things:
* Job name
* Job description
* Job image

Everything else will be semi-randomly generated if you don't supply it (though that can create results you may not want).

So, a basic screenshot can be created like so:

`python3 job.py --name "Club Vampire" --image dance.jpg --description "Vampire is working in a club near the beachfront. Hunter must find and kill. Client will meet once job is accepted. \$1000 bonus if job completed before July 4."`

And the results will look something like:
![Sample #iHunt job screenshot](sample.png)


There are lots of other options that can give you control over what the job looks like. To use any flag, it should start with two dashes, so to change the stars, you'd add something like `--stars 3.5`

| Flag | Use |
|--|--|
| `name` | (required) Name of job |
| `description` | (required) Description of job |
| `image` | (required) Image for card - will be resized to square if it's not already |
| `output` | Filename to save the screenshot to (default: job.png) |
| `price` | Price the job pays |
| `stars` | Numbers of stars for the job. Numbers between x.1 and x.9 become a half star. |
| `distance` | How far was the job created from your location? |
| `time` | How long ago was the job posted? |
| `remaining` | How much time is remaining to take this job? |

Some additional less common flags are avialable to further customize things, but you likely will need more rarely:

| Flag | Use |
|--|--|
| `currency` | Currency symbol for the job (default: $) |
| `distanceunit` | What is our unit of measure for distance (default: miles) |
| `timeunit` | Unit in time for how long ago the job was posted. (default: days) |
| `remainingunit` | Unit in time for how much time is remanining to accept this job. (default: days) |

You can get a basic list of these as well by running:

`python3 job.py --help`
