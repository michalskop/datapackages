# creates datapackage.json for each term


datapackage = {
    "name": "vaa-cz-" + town + "-2013-candidates-answers",
    "description": "Candidates' answers to VolebniKalkulacka.cz's (VAA) questions, Presidential elections 2013 in the Czech Republic",
    "resources": [
        {
            "name": "voters",
            "path":"data/voters.csv",
            "description": "Candidates",
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "type": "integer",
                        "description": "Candidates's id"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "description": "Candidates's name"
                    },
                    {
                        "name": "abbreviation",
                        "type": "string",
                        "description": "Candidates's abbreviation"
                    },
                    {
                        "name": "votes",
                        "type": "string",
                        "description": "indicator whether the candidate answered to the VAA questions"
                    }
                ],
                "primaryKey": "id"
            }
        },
        {
            "name": "vote_events",
            "path":"data/vote_events.csv",
            "description": "Questions of the VAA",
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "type": "integer",
                        "description": "questions's id"
                    },
                    {
                        "name": "motion:name",
                        "type": "string",
                        "description": "name of the question"
                    },
                    {
                        "name": "motion:text",
                        "type": "string",
                        "description": "question text"
                    },
                    {
                        "name": "motion:description",
                        "type": "string",
                        "description": "description of the question"
                    },
                    {
                        "name": "order",
                        "type": "integer",
                        "description": "order of the question in the VAA"
                    },
                    {
                        "name": "motion:text_candidates",
                        "type": "integer",
                        "description": "question text (as asked to the candidates)"
                    },
                    {
                        "name": "order_long",
                        "type": "integer",
                        "description": "order of the question in the long version of the VAA"
                    },
                    {
                        "name": "order_2",
                        "type": "integer",
                        "description": "order of the question in the VAA for the 2nd round of the elections"
                    }
                ],
                "primaryKey": "id"
            }
        },
        {
            "name": "votes",
            "path":"data/votes.csv",
            "description": "Candidates' answers to VAA's questions",
            "schema": {
                "fields": [
                    {
                        "name": "vote_event_id",
                        "type": "integer",
                        "description": "questions's id"
                    },
                    {
                        "name": "voter_id",
                        "type": "integer",
                        "description": "candidate's id"
                    },
                    {
                        "name": "option",
                        "type": "string",
                        "description": "candidate's answer"
                    },
                    {
                        "name": "explanation",
                        "type": "string",
                        "description": "candidate's explanation of the answer"
                    }
                ],
                "primaryKey": ["vote_event_id","voter_id"]
            }
        }
    ]
}
    
with open(directory + "/datapackage.json","w") as fout:
    json.dump(datapackage,fout)
    
readme = "# Candidates' answers to VolebniKalkulacka.cz's (VAA) questions, Presidential elections 2013 in the Czech Republic"

with open(directory + "/README.md","w") as fout:
    fout.write(readme)
