from pandas import read_csv, DataFrame
from court import Court


class Review:
    ser = 0
    reviewData = {}
    totalRatings = {}
    reviewedCourts = []
    generalRatings = {}

    def __init__(self, username, courtID, locatorID, locatorname, rating, review):
        self.username = username
        self.courtID = courtID
        self.locatorID = locatorID
        self.locatorname = locatorname
        self.rating = rating
        self.review = review
        self.id = __class__.ser
        __class__.ser += 1
        if courtID not in __class__.reviewedCourts:
            __class__.reviewedCourts.append(self.courtID)
            __class__.generalRatings[courtID] = rating
            __class__.totalRatings[courtID] = 0
        __class__.totalRatings[self.courtID] += 1
        self.updateCourtGeneralRating(courtID, rating)
        __class__.reviewData[self.id] = self.__dict__
        self.updateReviewData()

    @staticmethod
    def filterReviews():
        reviews = __class__.reviewData
        for review in reviews.items():
            review[1]['courtName'] = Court.getCourtName(
                int(review[1]['courtID']), int(review[1]['locatorID']))
        return reviews
        # courtID = courtName with court.Court.getCourtName(courtID)

    def updateReviewData(self):
        try:
            data = read_csv('reviewData/reviews.csv')
        except:
            data = DataFrame(
                columns=['id', 'username', 'courtID', 'locatorID', 'locatorname', 'rating', 'review'])
            data.to_csv('reviewData/reviews.csv', index=False)
        finally:
            data = read_csv('reviewData/reviews.csv')
            data.loc[self.id] = [self.id, self.username,
                                 self.courtID, self.rating, self.review]
            data.to_csv('reviewData/reviews.csv', index=False)

    @staticmethod
    def updateCourtGeneralRating(courtID, rating=0):
        print(rating)
        print(__class__.generalRatings)
        currentRating = __class__.generalRatings[courtID]
        print(currentRating)
        __class__.generalRatings[courtID] = (
            currentRating + rating) / __class__.totalRatings[courtID]
        print(__class__.generalRatings)
        try:
            reviewData = read_csv('reviewData/courtRatings.csv')
        except:
            reviewData = DataFrame(columns=['courtID', 'rating'])
            reviewData.to_csv('reviewData/courtRatings.csv', index=False)
        finally:
            reviewData = read_csv('reviewData/courtRatings.csv')
            reviewData.loc[courtID] = [
                courtID, __class__.generalRatings[courtID]]
            reviewData.to_csv('reviewData/courtRatings.csv', index=False)
