function adjustFooter() {
    var footer = document.querySelector('footer');
    var footerHeight = footer.offsetHeight;
    var bodyHeight = document.body.offsetHeight;
    var windowHeight = window.innerHeight;
    
    if (bodyHeight + footerHeight < windowHeight) {
        footer.classList.add('fixed-bottom');
    } else {
        footer.classList.remove('fixed-bottom');
    }
}


var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.type === 'childList') {
            adjustFooter();
        }
    });
});


var config = { childList: true, subtree: true };


observer.observe(document.body, config);
