# creates datapackage.json for each term


datapackage = {
    "name": "vaa-cz-" + town + "-2014-parties-answers",
    "description": "Parties' answers to VolebniKalkulacka.cz's (VAA) questions, European elections 2014 in the Czech Republic",
    "resources": [
        {
            "name": "voters",
            "path":"data/voters.csv",
            "description": "Parties",
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "type": "integer",
                        "description": "Party's id"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "description": "Party's name"
                    },
                    {
                        "name": "abbreviation",
                        "type": "string",
                        "description": "Party's abbreviation"
                    },
                    {
                        "name": "votes",
                        "type": "string",
                        "description": "indicator whether the party answered to the VAA questions"
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
                    }
                ],
                "primaryKey": "id"
            }
        },
        {
            "name": "votes",
            "path":"data/votes.csv",
            "description": "Parties' answers to VAA's questions",
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
                        "description": "party's id"
                    },
                    {
                        "name": "option",
                        "type": "string",
                        "description": "party's answer"
                    },
                    {
                        "name": "explanation",
                        "type": "string",
                        "description": "party's explanation of the answer"
                    }
                ],
                "primaryKey": ["vote_event_id","voter_id"]
            }
        }
    ]
}
    
with open(directory + "/datapackage.json","w") as fout:
    json.dump(datapackage,fout)
    
readme = "# Parties' answers to VolebniKalkulacka.cz's (VAA) questions, European elections 2014 in the Czech Republic"

with open(directory + "/README.md","w") as fout:
    fout.write(readme)
