from sqlalchemy import create_engine
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

engine  = create_engine("sqlite:///database.sqlite")

def base_player_data():

  df_soccer_data = pd.read_sql("""
    with df_date_table as ( \
        select  m.id as match_id, \
                hta.team_api_id as home_team_id, \
                ata.team_api_id as away_team_id, \
                m.date as match_date,
                max(hta.id) as ht_id, \
                max(ata.id) as at_id \
        from Match as m \
        join Team_Attributes as hta \
        on (m.home_team_api_id = hta.team_api_id) \
        join Team_Attributes as ata \
        on (m.away_team_api_id = ata.team_api_id) \
        where (m.date > hta.date) and (m.date > ata.date) \
        group by match_id, home_team_id, away_team_id, match_date) \
    select m.id as match_id, \
      m.country_id, \
      m.league_id, \
      m.season, \
      m.stage, \
      m.home_team_api_id as home_team_id, \
      m.away_team_api_id as away_team_id, \
      m.home_team_goal, \
      m.away_team_goal, \
      hta.buildUpPlaySpeed as home_buildUpPlaySpeed, \
      hta.buildUpPlayPassing as home_buildUpPlayPassing, \
      hta.chanceCreationPassing as home_chanceCreationPassing, \
      hta.chanceCreationShooting as home_chanceCreationShooting, \
      hta.defencePressure as home_defencePressure, \
      hta.defenceAggression as home_defenceAggression, \
      hta.defenceTeamWidth as home_defenceTeamWidth, \
      ata.buildUpPlaySpeed as away_buildUpPlaySpeed, \
      ata.buildUpPlayPassing as away_buildUpPlayPassing, \
      ata.chanceCreationPassing as away_chanceCreationPassing, \
      ata.chanceCreationShooting as away_chanceCreationShooting, \
      ata.defencePressure as away_defencePressure, \
      ata.defenceAggression as away_defenceAggression, \
      ata.defenceTeamWidth as away_defenceTeamWidth, \
      hp1.height as hp1_height, \
      hp2.height as hp2_height, \
      hp3.height as hp3_height, \
      hp4.height as hp4_height, \
      hp5.height as hp5_height, \
      hp6.height as hp6_height, \
      hp7.height as hp7_height, \
      hp8.height as hp8_height, \
      hp9.height as hp9_height, \
      hp10.height as hp10_height, \
      hp11.height as hp11_height, \
      ap1.height as ap1_height, \
      ap2.height as ap2_height, \
      ap3.height as ap3_height, \
      ap4.height as ap4_height, \
      ap5.height as ap5_height, \
      ap6.height as ap6_height, \
      ap7.height as ap7_height, \
      ap8.height as ap8_height, \
      ap9.height as ap9_height, \
      ap10.height as ap10_height, \
      ap11.height as ap11_height, \
      hp1.weight as hp1_weight, \
      hp2.weight as hp2_weight, \
      hp3.weight as hp3_weight, \
      hp4.weight as hp4_weight, \
      hp5.weight as hp5_weight, \
      hp6.weight as hp6_weight, \
      hp7.weight as hp7_weight, \
      hp8.weight as hp8_weight, \
      hp9.weight as hp9_weight, \
      hp10.weight as hp10_weight, \
      hp11.weight as hp11_weight, \
      ap1.weight as ap1_weight, \
      ap2.weight as ap2_weight, \
      ap3.weight as ap3_weight, \
      ap4.weight as ap4_weight, \
      ap5.weight as ap5_weight, \
      ap6.weight as ap6_weight, \
      ap7.weight as ap7_weight, \
      ap8.weight as ap8_weight, \
      ap9.weight as ap9_weight, \
      ap10.weight as ap10_weight, \
      ap11.weight as ap11_weight, \
      Julianday(m.date) - JulianDay(hp1.birthday) as hp1_age, \
      Julianday(m.date) - JulianDay(hp2.birthday) as hp2_age, \
      Julianday(m.date) - JulianDay(hp3.birthday) as hp3_age, \
      Julianday(m.date) - JulianDay(hp4.birthday) as hp4_age, \
      Julianday(m.date) - JulianDay(hp5.birthday) as hp5_age, \
      Julianday(m.date) - JulianDay(hp6.birthday) as hp6_age, \
      Julianday(m.date) - JulianDay(hp7.birthday) as hp7_age, \
      Julianday(m.date) - JulianDay(hp8.birthday) as hp8_age, \
      Julianday(m.date) - JulianDay(hp9.birthday) as hp9_age, \
      Julianday(m.date) - JulianDay(hp10.birthday) as hp10_age, \
      Julianday(m.date) - JulianDay(hp11.birthday) as hp11_age, \
      Julianday(m.date) - JulianDay(ap1.birthday) as ap1_age, \
      Julianday(m.date) - JulianDay(ap2.birthday) as ap2_age, \
      Julianday(m.date) - JulianDay(ap3.birthday) as ap3_age, \
      Julianday(m.date) - JulianDay(ap4.birthday) as ap4_age, \
      Julianday(m.date) - JulianDay(ap5.birthday) as ap5_age, \
      Julianday(m.date) - JulianDay(ap6.birthday) as ap6_age, \
      Julianday(m.date) - JulianDay(ap7.birthday) as ap7_age, \
      Julianday(m.date) - JulianDay(ap8.birthday) as ap8_age, \
      Julianday(m.date) - JulianDay(ap9.birthday) as ap9_age, \
      Julianday(m.date) - JulianDay(ap10.birthday) as ap10_age, \
      Julianday(m.date) - JulianDay(ap11.birthday) as ap11_age \
    from Match as m \
      join Country as c \
      on (c.id = m.country_id) \
      join League as l \
      on (l.id = m.league_id) \
      join Team as ht \
      on (m.home_team_api_id = ht.team_api_id) \
      join Team as at \
      on (m.home_team_api_id = at.team_api_id) \
      join Team_Attributes as hta \
      on (m.home_team_api_id = hta.team_api_id) \
      join Team_Attributes as ata \
      on (m.away_team_api_id = ata.team_api_id)\
      join df_date_table as ddt \
      on (m.id = ddt.match_id AND hta.id = ddt.ht_id AND ata.id = ddt.at_id) \
      left join player as hp1 \
      on (cast(m.home_player_1 as int) = hp1.player_api_id) \
      left join player as hp2 \
      on (cast(m.home_player_2 as int) = hp2.player_api_id) \
      left join player as hp3 \
      on (cast(m.home_player_3 as int) = hp3.player_api_id) \
      left join player as hp4 \
      on (cast(m.home_player_4 as int) = hp4.player_api_id) \
      left join player as hp5
      on (cast(m.home_player_5 as int) = hp5.player_api_id) \
      left join player as hp6 \
      on (cast(m.home_player_6 as int) = hp6.player_api_id) \
      left join player as hp7 \
      on (cast(m.home_player_7 as int) = hp7.player_api_id) \
      left join player as hp8 \
      on (cast(m.home_player_8 as int) = hp8.player_api_id) \
      left join player as hp9 \
      on (cast(m.home_player_9 as int) = hp9.player_api_id) \
      left join player as hp10 \
      on (cast(m.home_player_10 as int) = hp10.player_api_id) \
      left join player as hp11 \
      on (cast(m.home_player_11 as int) = hp11.player_api_id) \
      left join player as ap1 \
      on (cast(m.away_player_1 as int) = ap1.player_api_id) \
      left join player as ap2 \
      on (cast(m.away_player_2 as int) = ap2.player_api_id) \
      left join player as ap3 \
      on (cast(m.away_player_3 as int) = ap3.player_api_id) \
      left join player as ap4 \
      on (cast(m.away_player_4 as int) = ap4.player_api_id) \
      left join player as ap5 \
      on (cast(m.away_player_5 as int) = ap5.player_api_id) \
      left join player as ap6 \
      on (cast(m.away_player_6 as int) = ap6.player_api_id) \
      left join player as ap7 \
      on (cast(m.away_player_7 as int) = ap7.player_api_id) \
      left join player as ap8 \
      on (cast(m.away_player_8 as int) = ap8.player_api_id) \
      left join player as ap9 \
      on (cast(m.away_player_9 as int) = ap9.player_api_id) \
      left join player as ap10 \
      on (cast(m.away_player_10 as int) = ap10.player_api_id) \
      left join player as ap11 \
      on (cast(m.away_player_11 as int) = ap11.player_api_id) """, engine)

  return df_soccer_data

def base_player_agg(df):
    height_home = list(df.columns)[23:34]
    height_away = list(df.columns)[34:45]
    weight_home = list(df.columns)[45:56]
    weight_away = list(df.columns)[56:67]
    age_home = list(df.columns)[67:78]
    age_away = list(df.columns)[78:89]
    
    home_mean_height = df[height_home].mean(axis=1)
    away_mean_height = df[height_away].mean(axis=1)
    home_mean_weight = df[weight_home].mean(axis=1)
    away_mean_weight = df[weight_away].mean(axis=1)
    home_mean_age = df[age_home].mean(axis=1)
    away_mean_age = df[age_away].mean(axis=1)

    home_std_height = df[height_home].std(axis=1)
    away_std_height = df[height_away].std(axis=1)
    home_std_weight = df[weight_home].std(axis=1)
    away_std_weight = df[weight_away].std(axis=1)
    home_std_age = df[age_home].std(axis=1)
    away_std_age = df[age_away].std(axis=1)
    
    df_player = pd.concat([home_mean_height, away_mean_height, home_mean_weight,
                away_mean_weight, home_mean_age, away_mean_age, home_std_height,
                away_std_height, home_std_weight, away_std_weight, home_std_age,
                away_std_age], axis = 1)
    
    player_cols = ['home_mean_height', 'away_mean_height', 'home_mean_weight', 'away_mean_weight',
                     'home_mean_age', 'away_mean_age', 'home_std_height', 'away_std_height',
                     'home_std_weight', 'away_std_weight', 'home_std_age', 'away_std_age']
    df_player.columns = player_cols
    
    df = pd.concat([df, df_player], axis = 1)
    
    df = df.drop(columns=height_home)
    df = df.drop(columns=height_away)
    df = df.drop(columns=weight_home)
    df = df.drop(columns=weight_away)
    df = df.drop(columns=age_home)
    df = df.drop(columns=age_away)
    
    df = df.dropna(subset=player_cols)
    
    return df


def team_attributes_agg(df):
    build_up_home = ['home_buildUpPlaySpeed', 'home_buildUpPlayPassing', 'home_chanceCreationPassing', 'home_defencePressure']
    defense_home = ['home_defencePressure', 'home_defenceAggression', 'home_defenceTeamWidth']
    shooting_home = ['home_chanceCreationShooting']
    passing_home = ['home_buildUpPlayPassing', 'home_chanceCreationPassing']
    build_up_away = ['away_buildUpPlaySpeed', 'away_buildUpPlayPassing', 'away_chanceCreationPassing', 'away_defencePressure']
    defense_away = ['away_defencePressure', 'away_defenceAggression', 'away_defenceTeamWidth']
    shooting_away = ['away_chanceCreationShooting']
    passing_away = ['away_buildUpPlayPassing', 'away_chanceCreationPassing']
    
    home_mean_build_up = df[build_up_home].mean(axis=1)
    home_mean_defence = df[defense_home].mean(axis=1)
    home_mean_shooting = df[shooting_home].mean(axis=1)
    home_mean_passing = df[passing_home].mean(axis=1)
    away_mean_build_up = df[build_up_away].mean(axis=1)
    away_mean_defence = df[defense_away].mean(axis=1)
    away_mean_shooting = df[shooting_away].mean(axis=1)
    away_mean_passing = df[passing_away].mean(axis=1)
    
    home_std_build_up = df[build_up_home].std(axis=1)
    home_std_defence = df[defense_home].std(axis=1)
    home_std_passing = df[passing_home].std(axis=1)
    away_std_build_up = df[build_up_away].std(axis=1)
    away_std_defence = df[defense_away].std(axis=1)
    away_std_passing = df[passing_away].std(axis=1)
    
    df_team_attr = pd.concat([home_mean_build_up, home_mean_defence, home_mean_shooting, home_mean_passing,
                             away_mean_build_up, away_mean_defence, away_mean_shooting, away_mean_passing,
                             home_std_build_up, home_std_defence, home_std_passing,
                             away_std_build_up, away_std_defence, away_std_passing], axis=1)
    team_att_col = ['home_mean_build_up', 'home_mean_defence', 'home_mean_shooting', 'home_mean_passing',
                             'away_mean_build_up', 'away_mean_defence', 'away_mean_shooting', 'away_mean_passing',
                             'home_std_build_up', 'home_std_defence', 'home_std_passing',
                             'away_std_build_up', 'away_std_defence', 'away_std_passing']
    df_team_attr.columns = team_att_col
    
    df = pd.concat([df, df_team_attr], axis=1)
    
    # lists of columns overlaps, so errors should be ignored
    df = df.drop(columns=build_up_home, errors='ignore')
    df = df.drop(columns=defense_home, errors='ignore')
    df = df.drop(columns=shooting_home, errors='ignore')
    df = df.drop(columns=passing_home, errors='ignore')
    df = df.drop(columns=build_up_away, errors='ignore')
    df = df.drop(columns=defense_away, errors='ignore')
    df = df.drop(columns=shooting_away, errors='ignore')
    df = df.drop(columns=passing_away, errors='ignore')
    
    df = df.dropna(subset=team_att_col)
    
    return df

def process_data():
    df_soccer = base_player_data()
    df_soccer = base_player_agg(df_soccer)
    
    # set labels
    df_soccer['match_outcome'] = df_soccer.apply(lambda row: 1 if row['home_team_goal'] > row['away_team_goal'] else -1 if row['home_team_goal'] < row['away_team_goal'] else 0, axis=1)
    # drop unnecessary columns
    df_soccer = df_soccer.drop(columns=['home_team_goal', 'away_team_goal'])
    
    # apply OneHotEncoder to all categorical columns
    categorical_columns = ['season', 'country_id', 'league_id', 'home_team_id', 'away_team_id']
    encoder = OneHotEncoder(sparse=False, handle_unknown = 'ignore')
    encoded_columns = encoder.fit_transform(df_soccer[categorical_columns])
    encoded_df = pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(categorical_columns))
    df_soccer = df_soccer.drop(columns=categorical_columns).reset_index(drop=True)
    df_soccer = pd.concat([df_soccer, encoded_df], axis=1)    
    
    return df_soccer