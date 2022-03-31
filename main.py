from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки кандидата - {candidate["skills"]}\n\n'
    str_candidates += '</pre>\n'

    return str_candidates

@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f'<img src={candidate["picture"]}><br><br>Имя кандидата - {candidate["name"]}<br>Позиция кандидата  - {candidate["position"]}<br>Навыки кандидата - {candidate["skills"]}'

    return str_candidates


@app.route("/skills/<skill>")
def profile_skills(skill):
    str_candidates = "<pre>"

    for candidate in candidates.values():
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill.lower() in candidate_skills:
            str_candidates += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки кандидата - {candidate["skills"]}\n\n'
    str_candidates += "</pre>"

    return str_candidates
# app.add_url_rule('/', view_func=page_index)

app.run()
