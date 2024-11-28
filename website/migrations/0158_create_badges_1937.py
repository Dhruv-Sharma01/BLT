# Generated by Django 5.1.3 on 2024-11-27 19:37

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def create_badges(apps, schema_editor):
    # Get the Badge and User models
    Badge = apps.get_model("website", "Badge")
    User = apps.get_model("auth", "User")
    UserBadge = apps.get_model("website", "UserBadge")

    # List of badges to create (title and description)
    badges = [
        # Manual Badges (Awarded manually by a mentor or admin)
        {
            "title": "Mentor",
            "description": "Awarded to users who serve as mentors.",
            "type": "manual",
            # eg: "icon": "badges/mentor_badge.png",
        },
        # GitHub-related Automatic Badges
        {
            "title": "First Pull Request Merged",
            "description": "Awarded when the first pull request is merged.",
            "type": "automatic",
        },
        {
            "title": "First Contribution",
            "description": "Awarded when the first code contribution is made.",
            "type": "automatic",
        },
        {
            "title": "First Code Review",
            "description": "Awarded when the first code review is submitted.",
            "type": "automatic",
        },
        {
            "title": "First Documentation Contribution",
            "description": "Awarded when the first documentation contribution is made.",
            "type": "automatic",
        },
        {
            "title": "First Test Added",
            "description": "Awarded when the first test is added to the codebase.",
            "type": "automatic",
        },
        {
            "title": "First Issue Closed",
            "description": "Awarded when the first issue is closed.",
            "type": "automatic",
        },
        {
            "title": "First Pull Request Reviewed",
            "description": "Awarded when the first pull request is reviewed.",
            "type": "automatic",
        },
        {
            "title": "First Milestone Achieved",
            "description": "Awarded when the first milestone is achieved.",
            "type": "automatic",
        },
        {
            "title": "First CI Build Passed",
            "description": "Awarded when the first CI build passes.",
            "type": "automatic",
        },
        {
            "title": "First CI Build Failed",
            "description": "Awarded when the first CI build fails.",
            "type": "automatic",
        },
        {
            "title": "First Security Issue Reported",
            "description": "Awarded when the first security issue is reported.",
            "type": "automatic",
        },
        {
            "title": "First Security Fix Merged",
            "description": "Awarded when the first security fix is merged.",
            "type": "automatic",
        },
        {
            "title": "First Code Linter Passed",
            "description": "Awarded when the first code linter check passes.",
            "type": "automatic",
        },
        {
            "title": "First Code Linter Failed",
            "description": "Awarded when the first code linter check fails.",
            "type": "automatic",
        },
        {
            "title": "First Dependency Updated",
            "description": "Awarded when the first dependency is updated.",
            "type": "automatic",
        },
        {
            "title": "First Fork Created",
            "description": "Awarded when the first fork is created.",
            "type": "automatic",
        },
        {
            "title": "First Star Given",
            "description": "Awarded when the first star is given to a repository.",
            "type": "automatic",
        },
        {
            "title": "First Branch Created",
            "description": "Awarded when the first branch is created.",
            "type": "automatic",
        },
        {
            "title": "First Tag Created",
            "description": "Awarded when the first tag is created.",
            "type": "automatic",
        },
        {
            "title": "First Commit",
            "description": "Awarded when the first commit is made.",
            "type": "automatic",
        },
        {
            "title": "First Merge Conflict Resolved",
            "description": "Awarded when the first merge conflict is resolved.",
            "type": "automatic",
        },
        {
            "title": "First Code Refactor",
            "description": "Awarded when the first code refactor is done.",
            "type": "automatic",
        },
        {
            "title": "First Code Optimization",
            "description": "Awarded when the first code optimization is made.",
            "type": "automatic",
        },
        {
            "title": "First Performance Improvement",
            "description": "Awarded when the first performance improvement is made.",
            "type": "automatic",
        },
        # Site-related Badges
        {
            "title": "First Bug Reported",
            "description": "Awarded when the first bug is reported.",
            "type": "automatic",
        },
        {
            "title": "First Blog Posted",
            "description": "Awarded when the first blog post is published.",
            "type": "automatic",
        },
        {
            "title": "First Discussion Started",
            "description": "Awarded when the first discussion is started.",
            "type": "manual",
        },
        {
            "title": "First Project Board Created",
            "description": "Awarded when the first project board is created.",
            "type": "manual",
        },
        {
            "title": "First Project Board Completed",
            "description": "Awarded when the first project board is completed.",
            "type": "manual",
        },
        {
            "title": "First Wiki Page Created",
            "description": "Awarded when the first wiki page is created.",
            "type": "manual",
        },
        {
            "title": "First Wiki Page Edited",
            "description": "Awarded when the first wiki page is edited.",
            "type": "manual",
        },
        {
            "title": "First API Documentation Added",
            "description": "Awarded when the first API documentation is added.",
            "type": "manual",
        },
        {
            "title": "First Markdown File Added",
            "description": "Awarded when the first markdown file is added.",
            "type": "manual",
        },
        {
            "title": "First Community Event Hosted",
            "description": "Awarded when the first community event is hosted.",
            "type": "manual",
        },
        {
            "title": "First Demo Recorded",
            "description": "Awarded when the first demo is recorded.",
            "type": "manual",
        },
        {
            "title": "First Tutorial Published",
            "description": "Awarded when the first tutorial is published.",
            "type": "manual",
        },
        {
            "title": "First Webinar Hosted",
            "description": "Awarded when the first webinar is hosted.",
            "type": "manual",
        },
        {
            "title": "First Meetup Organized",
            "description": "Awarded when the first meetup is organized.",
            "type": "manual",
        },
        {
            "title": "First Conference Talk",
            "description": "Awarded when the first conference talk is delivered.",
            "type": "manual",
        },
        {
            "title": "First Newsletter Sent",
            "description": "Awarded when the first newsletter is sent.",
            "type": "manual",
        },
        {
            "title": "First Social Media Post",
            "description": "Awarded when the first social media post is made.",
            "type": "manual",
        },
        {
            "title": "First Community Survey",
            "description": "Awarded when the first community survey is conducted.",
            "type": "manual",
        },
        {
            "title": "First User Feedback",
            "description": "Awarded when the first user feedback is received.",
            "type": "manual",
        },
    ]
    # Create the badges
    for badge in badges:
        icon = badge.get("icon", None)
        badge_obj, created = Badge.objects.get_or_create(
            title=badge["title"],
            defaults={
                "description": badge["description"],
                "type": badge["type"],
                "icon": icon,
            },
        )
        print(f"Badge '{badge['title']}' created: {created}")

    try:
        user = User.objects.get(username="donnie")
    except ObjectDoesNotExist:
        print("User 'donnie' does not exist. Skipping the assignment of the Mentor badge.")
    else:
        # Get the "Mentor" badge (make sure it's created first)
        mentor_badge = Badge.objects.get(title="Mentor")
        # Get or create the UserBadge association for this user and the "Mentor" badge
        user_badge, created = UserBadge.objects.get_or_create(user=user, badge=mentor_badge)
        print(f"Assigned 'Mentor' badge to user '{user.username}': {created}")


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0157_badge_userbadge"),
    ]

    operations = [
        migrations.RunPython(create_badges),
    ]