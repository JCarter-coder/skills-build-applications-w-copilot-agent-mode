# Test data for populating the octofit_db database

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team"},
    {"name": "Gold Team"},
]

test_activities = [
    {"activity_type": "Cycling", "duration": "01:00:00"},
    {"activity_type": "Crossfit", "duration": "02:00:00"},
    {"activity_type": "Running", "duration": "01:30:00"},
    {"activity_type": "Strength", "duration": "00:30:00"},
    {"activity_type": "Swimming", "duration": "01:15:00"},
]

test_leaderboard = [
    {"score": 100},
    {"score": 90},
    {"score": 95},
    {"score": 85},
    {"score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]