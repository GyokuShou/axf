// 顶部轮播图
$(function(){
    var swiper = new Swiper('#top-swiper', {
    pagination: '.swiper-pagination',
    slidesPerView: 1,
    paginationClickable: true,
    spaceBetween: 30,
    loop: true,
    autoplay: 4000
    });
});
// 顶部轮播图结束


// 必购js
$(function(){
    var swiper = new Swiper('#mustbuy-swiper', {
    pagination: '.swiper-pagination',
    slidesPerView: 3,
    // paginationClickable: true,
    spaceBetween: 5,
    loop: true,
    });
});
// 必购js结束

$(function(){
    $('.home').width(innerWidth);
});