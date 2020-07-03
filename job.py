import argparse
import random

import ihuntapp


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Build an #iHunt job app page.')
    parser.add_argument('--name', "-n",
                        default="Unnamed job", help='Name of the job')
    parser.add_argument('--description', "-d",
                        default="No description available", help='Description of the job')
    parser.add_argument('--image', "-i",
                        type=str, default="", help='Job image', required=True)
    parser.add_argument('--price', "-p",
                        default=(random.randint(1, 18) * 500), help='Price the job pays')
    parser.add_argument('--stars', "-s",
                        type=float, default=(random.randint(3, 8) * 0.5), help='Star level of job')
    parser.add_argument('--currency', default="$", help='Currency symbol')
    parser.add_argument('--distance',
                        type=float, default=random.uniform(5, 25), help='Distance of job')
    parser.add_argument('--distanceunit', default="miles", help='distance unit')
    parser.add_argument('--time', "-t",
                        type=float, default=random.randint(1, 3), help='Time of post')
    parser.add_argument('--timeunit', default="days", help='Time unit')
    parser.add_argument('--remaining', "-r",
                        type=float, default=random.randint(3, 8), help='Time of post')
    parser.add_argument('--remainingunit', default="days", help='Time unit')

    parser.add_argument('--output', '-o', default='job.png', help='Filename to save screenshot')
    args = parser.parse_args()

    phone = ihuntapp.iHuntApp(args.name, args.description, args.image)
    phone.price = args.price
    phone.stars = args.stars
    phone.currency = args.currency
    phone.distance = args.distance
    phone.distanceunit = args.distanceunit
    phone.time = args.time
    phone.timeunit = args.timeunit
    phone.remaining = args.remaining
    phone.remainingunit = args.remainingunit

    phone.screenshot(args.output)
