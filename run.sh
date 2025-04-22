# run.sh
results=./kinopoisk-result
rep_history=./kinopoisk-report/history
report=./kinopoisk-report

rm -rf $results
pytest --alluredir=$results
mv $rep_history $results
rm -rf $report
allure generate $results -o $report
allure open $report
