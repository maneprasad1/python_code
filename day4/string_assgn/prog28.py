import textwrap
para = """Nature around us is a gift. We need to handle it wisely.
Nature's gift are for everyone and many generations. Every generation,
need to think before making a damage to these gifts."""

res = textwrap.dedent(para)
wrapped = textwrap.fill(res, width = 50)
final = textwrap.indent(wrapped, 'line ')
print(final)
