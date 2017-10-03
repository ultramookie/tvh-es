# tvh-es

Stash tvheadend recording information and stats in Elasticsearch for fun.

I use this along with the tvh-wrapper.sh script so that I can put it as part of the post-processing step and have filebot run against the recorded file also. But, it can be called directly also. Just pass in the right variables (listed in both scripts).

Do fun things like:

* Graph the data and transport errors per channel over time.
* Graph the time spent recording per channel.
* Graph the time spent recording per show.
* Graph the most common time of day for recording.
* Graph the most popular channel.

Stuff like that.
