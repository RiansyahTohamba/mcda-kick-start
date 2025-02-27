# getting started
Multi criteria decision aids (MCDA) help us in decision making. 
There are several names for MCDA which likes:
1. SISTEM PENDUKUNG KEPUTUSAN and so on.

# CLI based MCDA
CLI Football example is one of example CLI based MCDA.

# WEB based MCDA
Web based MCDA is WEB based version of CLI Football example.
Just give it a try!

# install dependencies
pip install -r requirements.txt

# steps
1. buat table
python models/create_table.py

2. transfer data dari CSV ke table
python seed.py

3. running main apps
python waspas_rank_pl.py