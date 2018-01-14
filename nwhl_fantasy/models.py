# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


#class AuthGroup(models.Model):
#    name = models.CharField(unique=True, max_length=80)
#
#    class Meta:
##        managed = False
#        db_table = 'auth_group'
#
#
#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#    class Meta:
##        managed = False
#        db_table = 'auth_group_permissions'
#        unique_together = (('group', 'permission'),)
#
#
#class AuthPermission(models.Model):
#    name = models.CharField(max_length=255)
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#    codename = models.CharField(max_length=100)
#
#    class Meta:
##        managed = False
#        db_table = 'auth_permission'
#        unique_together = (('content_type', 'codename'),)
#
#
#class AuthUser(models.Model):
#    password = models.CharField(max_length=128)
#    last_login = models.DateTimeField(blank=True, null=True)
#    is_superuser = models.BooleanField()
#    username = models.CharField(unique=True, max_length=150)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.CharField(max_length=254)
#    is_staff = models.BooleanField()
#    is_active = models.BooleanField()
#    date_joined = models.DateTimeField()
#
#    class Meta:
##        managed = False
#        db_table = 'auth_user'
#
#
#class AuthUserGroups(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#    class Meta:
##        managed = False
#        db_table = 'auth_user_groups'
#        unique_together = (('user', 'group'),)
#
#
#class AuthUserUserPermissions(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#    class Meta:
##        managed = False
#        db_table = 'auth_user_user_permissions'
#        unique_together = (('user', 'permission'),)
#
#
#class DjangoAdminLog(models.Model):
#    action_time = models.DateTimeField()
#    object_id = models.TextField(blank=True, null=True)
#    object_repr = models.CharField(max_length=200)
#    action_flag = models.SmallIntegerField()
#    change_message = models.TextField()
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#    class Meta:
##        managed = False
#        db_table = 'django_admin_log'
#
#
#class DjangoContentType(models.Model):
#    app_label = models.CharField(max_length=100)
#    model = models.CharField(max_length=100)
#
#    class Meta:
##        managed = False
#        db_table = 'django_content_type'
#        unique_together = (('app_label', 'model'),)
#
#
#class DjangoMigrations(models.Model):
#    app = models.CharField(max_length=255)
#    name = models.CharField(max_length=255)
#    applied = models.DateTimeField()
#
#    class Meta:
##        managed = False
#        db_table = 'django_migrations'
#
#
#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#
#    class Meta:
##        managed = False
#        db_table = 'django_session'


class GoalieStatsGame(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    matchup = models.ForeignKey('Schedules', models.DO_NOTHING)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    pen_mins = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    shots_against = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'goalie_stats_game'


class GoalieStatsSeason(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    goals_against = models.IntegerField(blank=True, null=True)
    shots_against = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    shoot_out_losses = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'goalie_stats_season'


class Leagues(models.Model):
    league_id = models.AutoField(primary_key=True)
    league_name = models.TextField()
    num_teams = models.IntegerField()

    class Meta:
#        managed = False
        db_table = 'leagues'


class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    team = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    health = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.TextField()
    num = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'players'


class Schedules(models.Model):
    matchup_id = models.AutoField(primary_key=True)
    week_num = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING, blank=True, null=True)
    home_team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='home_team', blank=True, null=True, related_name='%(class)s_team_id')
    away_team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='away_team', blank=True, null=True)
    home_points = models.IntegerField(blank=True, null=True)
    away_points = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'schedules'


class SkaterStatsMatchup(models.Model):
    player = models.ForeignKey(Players, models.DO_NOTHING, primary_key=True)
    matchup = models.ForeignKey(Schedules, models.DO_NOTHING)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)
    pen_mins = models.IntegerField(blank=True, null=True)
    power_play_goals = models.IntegerField(blank=True, null=True)
    power_play_assists = models.IntegerField(blank=True, null=True)
    shorthanded_goals = models.IntegerField(blank=True, null=True)
    shorthanded_assists = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'skater_stats_matchup'


class SkaterStatsSeason(models.Model):
    player = models.ForeignKey(Players, models.DO_NOTHING, primary_key=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)
    pen_mins = models.IntegerField(blank=True, null=True)
    power_play_goals = models.IntegerField(blank=True, null=True)
    power_play_assists = models.IntegerField(blank=True, null=True)
    short_handed_goals = models.IntegerField(blank=True, null=True)
    short_handed_assists = models.IntegerField(blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)
    sog = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    faceoffs_won = models.IntegerField(blank=True, null=True)
    faceoffs_lost = models.IntegerField(blank=True, null=True)
    blocked_shots = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'skater_stats_season'


class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    team_name = models.TextField()
    fwd1 = models.ForeignKey(Players, models.DO_NOTHING, db_column='fwd1', blank=True, null=True, related_name='%(class)s_player_id_fwd1')
    fwd2 = models.ForeignKey(Players, models.DO_NOTHING, db_column='fwd2', blank=True, null=True, related_name='%(class)s_player_id_fwd2')
    fwd3 = models.ForeignKey(Players, models.DO_NOTHING, db_column='fwd3', blank=True, null=True, related_name='%(class)s_player_id_fwd3')
    def1 = models.ForeignKey(Players, models.DO_NOTHING, db_column='def1', blank=True, null=True, related_name='%(class)s_player_id_def1')
    def2 = models.ForeignKey(Players, models.DO_NOTHING, db_column='def2', blank=True, null=True, related_name='%(class)s_player_id_def2')
    util = models.ForeignKey(Players, models.DO_NOTHING, db_column='util', blank=True, null=True, related_name='%(class)s_player_id_util')
    bench1 = models.ForeignKey(Players, models.DO_NOTHING, db_column='bench1', blank=True, null=True, related_name='%(class)s_player_id_bench1')
    bench2 = models.ForeignKey(Players, models.DO_NOTHING, db_column='bench2', blank=True, null=True, related_name='%(class)s_player_id_bench2')
    bench3 = models.ForeignKey(Players, models.DO_NOTHING, db_column='bench3', blank=True, null=True, related_name='%(class)s_player_id_bench3')
    bench4 = models.ForeignKey(Players, models.DO_NOTHING, db_column='bench4', blank=True, null=True, related_name='%(class)s_player_id_bench4')
    goalie = models.ForeignKey(Players, models.DO_NOTHING, db_column='goalie', blank=True, null=True, related_name='%(class)s_player_id_goalie')
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    points_for = models.IntegerField(blank=True, null=True)
    points_against = models.IntegerField(blank=True, null=True)
    standings_points = models.IntegerField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'teams'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField(unique=True)
    pword = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(unique=True)
    
    def __str__(self):
        return str(self.username)

    class Meta:
#        managed = False
        db_table = 'users'
