const $portfolio = document.querySelector('.sec-portfolio-js');
const $modalImgPortfolio = document.querySelector('.img-modal-js');


$portfolio.addEventListener('click', (e) => {
    // console.log(e.target);
    // console.log(e.targer.classlist);
    if (e.target.classList.contains('img-btn-modal-js')){
        // SRC
        let urlImg = e.target.getAttribute('src');

        // Add to modal
        $modalImgPortfolio.src = urlImg;
    };
});


