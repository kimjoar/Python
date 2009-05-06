import difflib, re

def inline_diff(text1, text2):
  text = []
  for word in list(difflib.ndiff(text1.split(), text2.split())):
    if re.match("\+ ", word):
      text.append("(+" + word[2:] + ")")
    elif re.match("- ", word):
      text.append("(-" + word[2:] + ")")
    elif re.match("  ", word):
      text.append(word[2:])
  return " ".join(text)

text1 = "Unified diffs are a compact way of showing just the lines that have changed plus a few lines of context."
text2 = "Unified diffs are a compact way of showing just the lins have changed plus a few linesor of context."

print inline_diff(text1, text2)