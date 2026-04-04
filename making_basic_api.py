import requests

# GET request
# posts = requests.get("https://jsonplaceholder.typicode.com/posts")
# comments = requests.get("https://jsonplaceholder.typicode.com/comments")
# albums = requests.get("https://jsonplaceholder.typicode.com/ablums")
# photos = requests.get("https://jsonplaceholder.typicode.com/photos")
#
#
#
# for post in posts.json():
#     print(post)
#
# for comment in comments.json():
#     print(comment)
#
#
# # POST request
# post_response = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json={"userId": 12, "title": "Test Title", "body": "Test Body"},
# )
#
# print(post_response.status_code)
# print(post_response.json())
# print(post_response.json())
#
# # PUT request
# put_response = requests.put(
#     "https://jsonplaceholder.typicode.com/posts/10",
#     json={"userId": 13, "id": 1, "title": "Updated Title", "body": "Updated Body"},
# )
#
# print(put_response.status_code)
#
# # PATCH request
# patch_response = requests.put(
#     "https://jsonplaceholder.typicode.com/posts/1",
#     json={"userId": 101},
# )
#
# print(patch_response.status_code)
# print(patch_response.json())
# print(requests.get("https://jsonplaceholder.typicode.com/posts/1").json())
#
# # DELETE request
# delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
#
# print(delete_response.status_code)
# print(delete_response.json())

# print(
#     requests.get(
#         "https://jsonplaceholder.typicode.com/posts/", params={"id": 1}
#     ).content
# )
#

# r = requests.get("https://jsonplaceholder.typicode.com/posts", stream=True)
#
# print(r.raw)

# print(r.raw.read(10))

# filename = "reponse.txt"
# with open(filename, "wb") as fd:
#     for chunk in r.iter_content(chunk_size=64):
#         fd.write(chunk)
#
# print(r.headers)
