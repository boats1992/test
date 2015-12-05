# Get movie lists from search page
def searchMovie(url):
	href_queue = []
	head = 0

	# Get movie hrefs and names
	(movie_href, movie_name) = parseSearchPage(url)

	for index in range(len(movie_href)):
		movie_link = HOST_URL + movie_href[index]
		href_queue.append({'href': movie_link, 'dist': 0})
		#print movie_name[index] + ", " + movie_link

	while (head <= len(href_queue)):
		cur = href_queue[head]
		info = getMovieInfo(cur['href'], cur['dist'])
		head += 1
		if info == None:
			continue

		print 'Title: ' + info['title'] + '\ndist: ' + str(cur['dist']) + \
				'\nYear: ' + str(info['year']) + '\nRating: ' + str(info['rating']) + \
				'\nDirector: ' + str(info['director']) + \
				'\nCast: ' + str(info['cast'])
		print
		
		for cast_href in info['cast_href']:
			movies = parseCastPage(cast_href)
			if movies == None:
				continue
			for movie in movies['movie_href']:
				href_queue.append({'href': movie, 'dist': cur['dist'] + 1})

		time.sleep(1)
		#print href_queue
