document.addEventListener('DOMContentLoaded', function () {                             // This is a callback function that will be called when the DOM is ready
    const categoryButtons = document.querySelectorAll('.category-buttons a');           // Get all the category buttons
    const postsList = document.querySelector('.posts');                                 // Get the posts list


    categoryButtons.forEach(button => {                                                 // Loop through each button
        button.addEventListener('click', function (e) {                                 // Add a click event listener to each button
            e.preventDefault();                                                         // Prevent the default action of the link
            console.log("Button clicked:", this);                                       // For debugging
            const categorySlug = this.dataset.categorySlug;                             // Get the category slug from the data-category-slug attribute
            console.log("Category slug:", categorySlug);                                // For debugging
            fetch(`/get_filtered_posts/?category=${categorySlug}`)                      // Fetch the posts for the selected category using the category slug
                .then(response => response.json())                                      // Convert the response to JSON format and return it as a promise
                .then(data => {                                                         // Process the JSON data in the response
                    postsList.innerHTML = '';                                           // Clear out the old posts
                    console.log("Fetched posts:", data);                                // For debugging

                    data.forEach(post => {                                              // Loop through each post
                        const postItem = document.createElement('div');                 // Create a new post item element
                        postItem.className = 'post';                                    // Add a class to the post item element
                                                                                        // Add the post item HTML to the post item element
                        postItem.innerHTML = `                                          
                            <div class="content-wrap">
                                <div class="hero__shape-2"></div>
                                <div class="hero__shape-3"></div>
                                <h2><a href="/post/${post.pk}/">${post.title}</a></h2>
                                <p>${post.category.join(", ")}</p>
                                <div class="post_img" style="text-align: center;">
                                    <img style='width: 140px; height: 140px; display: inline-block;'
                                     src="/static/img/glucose.png" alt="">
                                </div>
                                <p>${post.body}</p>
                                <h5>Author: ${post.author}</h5>
                            </div>
                        `;

                        postsList.appendChild(postItem);                                // Add the post item element to the posts list
                    });
                })
                .catch(error => {                                                       // Catch any errors and log them to the console
                    console.error('Error:', error);
                });
        });
    });
});
