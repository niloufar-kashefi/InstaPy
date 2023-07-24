from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'Exmodules'
insta_password = '004366565617664@Exmodule'

comments = ['Useful @{}',
        'You are greate @{}',
        'thanks, good information',
        'GUYSSSSSSSS, I am a person who follow back, like, comment,... direct me',
        'I am your fan @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yeeeeeees!',
        'Guys, I am ready for interact, like, follow, comment',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)


with smart_run(session):

  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])	
  session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21) #delay
  session.set_relationship_bounds(enabled=True, max_followers=8500)  #won’t interact with posts by users who have more than 8,500 followers	
  #session = InstaPy(username='test', password='test', headless_browser=True)   ///without GUI on server
  
  # activity		
  session.like_by_tags(["nft", "cryptocurrency"], amount=5)
  session.set_dont_like(["naked", "nsfw"])
  session.set_do_follow(True, percentage=50)
  session.set_do_comment(True, percentage=50) #follow the people coment on that post
  session.set_comments(comments)

  # Joining Engagement Pods
  #session.join_pods(topic='cryptocurrency', engagement_mode='no_comments')

















