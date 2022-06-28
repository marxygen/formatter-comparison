from flask import Flask, render_template, request, flash
import black
import yapf

app = Flask(__name__)
app.secret_key = "skefhesjhJHSEJFsjhfg3jrghwefyitusegfsvghj"


@app.route("/")
def comparator():
    to_be_formatted = '''a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

ImportantClass.important_method(exc, limit, lookup_lines, capture_locals, extra_argument)

def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        ...

if some_short_rule1 \
  and some_short_rule2:
      ...
# Note the trailing commas
TRANSLATIONS = {
    "en_us": "English (US)",
    "pl_pl": "polski",
}
    '''
    black_format = yapf_format = "Not formatted"

    return render_template(
        "comparison.html",
        to_be_formatted=to_be_formatted,
        black_format=black_format,
        yapf_format=yapf_format,
    )


@app.route("/format", methods=["POST"])
def format_code():
    code = request.json["code"]
    errors = ""
    black_format = yapf_format = "Not formatted"

    try:
        black_format = black.format_str(code, mode=black.Mode())
        yapf_format = yapf.yapf_api.FormatCode(code)[0]
    except Exception as e:
        errors += "Exception: " + str(e) + "; Check that Python code is correct\n"

    return {
        "black": black_format,
        "yapf": yapf_format,
        "errors": errors,
    }


# app.run(debug=True, host="0.0.0.0", port=8080)
