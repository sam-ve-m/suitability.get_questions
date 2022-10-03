#!/bin/bash
fission spec init
fission env create --spec --name suitability-questions-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name suitability-questions-fn --env suitability-questions-env --src "./func/*" --entrypoint main.get_suitability_questions --executortype newdeploy --maxscale 3
fission route create --spec --name suitability-questions-rt --method GET --url /suitability/questions --function suitability-questions-fn
