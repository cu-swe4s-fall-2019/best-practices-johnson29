test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py -i data.txt -c 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py -i data.txt -c 2

run test1 python get_column_stats.py -i data.txt -c 5
assert_in_stdout "mean: 1.0"
assert_in_stdout "stdev: 0.0"
assert_exit_code 0

run test2 python get_column_stats.py -i data.txt -c 0
assert_in_stdout "invalid column #"
assert_exit_code 1

run test3 python get_column_stats.py -i whatever.txt -c 3
assert_in_stdout "file open error"
assert_exit_code 1
