# Shop demo chatbots

A make.fun entry for "The plan make.fun will carry out in public".

`main.py` writes one plan to `/output/entry.txt`: on day 1, find small
shops on Google Maps with no chat support, build each a demo chatbot in
minutes, and email them a live link with a $199 setup fee and a
$29/month Stripe link. The $100 covers hosting and email credits.

Run it with:

```sh
python3 main.py
```

It writes the entry deterministically (same bytes on every run) and
validates that the entry is 1–280 Unicode code points and not only
whitespace.
