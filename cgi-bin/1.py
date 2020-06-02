import sys

fieldnames = ('name', 'age', 'job', 'pay')

replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch", name=action>
    <input type=submit value="Update", name=action>
</form>
</body></html>
"""

# вставить разметку html с данными в позицию $ROWS$
rowhtml = '<tr><th>%s<td><input type=text name=%s value"%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()                          # значения могут содержать &, >
    for field in fieldnames:                    # и другие специальные символы,
        value = new[field]                      # отображаемые особым образом;
        new[field] = html.escape(repr(value))   # их необходимо экранировать
    return new

print(replyhtml % htmlize(fields)) 
sys.exit()
