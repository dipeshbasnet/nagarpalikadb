import datetime
import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django.utils import timezone

from apps.core.models import Business
from apps.core.seeder_constants import SURNAMES, MALE_NAMES

USER = get_user_model()


def get_random_dob():
    from datetime import date
    start_dt = date.today().replace(year=1953, day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day


def get_random_business_name():
    prefix = ['Awiskaar', 'Cotiviti', 'Dev Async', 'Kritya', 'Anup', 'Hard Hat', 'Switch', 'Outsight', 'Gloves',
              'Jhola', 'Sanjay', 'Try Again']
    suffix = ['Solutions', 'Pvt Ltd', 'Suppliers', 'LLC', 'And Partners']

    return f"{random.choice(prefix)} {random.choice(suffix)}"


class Command(BaseCommand):
    help = 'seed initial data'

    def handle(self, *args, **options):
        user_objs = []
        month_now = datetime.datetime.today().month
        for _ in range(50):
            random_gender = random.choice(["MALE", "FEMALE"])
            first_name = random.choice(MALE_NAMES) if random_gender == "MALE" else random.choice(MALE_NAMES)
            username = f"{first_name}{random.randint(0, 100)}{random.randint(100, 99999)}"
            user_dict = dict(
                username=username,
                email=f"{username}@gmail.com",
                first_name=first_name,
                last_name=random.choice(SURNAMES),
                is_active=True,
                # gender=random_gender,
                # account_status="APPROVED",
                # dob=get_random_dob(),
                # created_at=timezone.now().replace(month=random.randint(1, month_now))
            )
            owner = USER.objects.create(**user_dict)
            business_name = get_random_business_name()
            bis_email = business_name.replace(" ", "")
            business_dict = dict(
                name=get_random_business_name(),
                reg_number=random.randint(111111, 999999),
                status='APPROVED',
                type=random.choice(['PVT LTD', 'Domestic', 'Others']),
                capital_amt=random.choice([100000, 500000, 1000000]),
                email=f"info@{bis_email}.com",
                municipality="Kathmandu",
                street=random.choice(["Gongabu", 'Naxal', 'Gairidhara', 'Newroad', 'Dhumbarahi']),
                contact_no=f"{random.choice([9861, 9841, 9843])}{random.randint(111111, 999999)}",
                mobile_no=f"{random.choice([9861, 9841, 9843])}{random.randint(111111, 999999)}",
                house_no=random.randint(1, 1000),
                ward=random.randint(1, 15),
                signboard_size_length='4',
                signboard_size_width='4',
                created_at=timezone.now().replace(month=random.randint(1, month_now))
            )
            business = Business.objects.create(**business_dict)
            business.owner.add(owner)
        print('Complete!')
