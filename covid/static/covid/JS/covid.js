const test = document.querySelector('.tes');
  const conf = document.querySelector('.con');
  const acti = document.querySelector('.act');
  const reco = document.querySelector('.rec');
  const deat = document.querySelector('.dea');
  
  conf.addEventListener('click',()=>{
    test.style.backgroundColor = "#fff";
    conf.style.backgroundColor = "rgba(255, 0, 0, 0.2)";
    acti.style.backgroundColor = "#fff";
    reco.style.backgroundColor = "#fff";
    deat.style.backgroundColor = "#fff";
    document.querySelector('.conf').style.display = "block";
    document.querySelector(".acti").style.display = "none";
    document.querySelector('.reco').style.display = "none";
    document.querySelector('.deat').style.display = "none";
  });

  acti.addEventListener('click',()=>{
    test.style.backgroundColor = "#fff";
    conf.style.backgroundColor = "#fff";
    acti.style.backgroundColor = "rgba(0, 112, 216, 0.2)";
    reco.style.backgroundColor = "#fff";
    deat.style.backgroundColor = "#fff";
    document.querySelector('.conf').style.display = "none";
    document.querySelector('.acti').style.display = "block";
    document.querySelector('.reco').style.display = "none";
    document.querySelector('.deat').style.display = "none";
  });

  reco.addEventListener('click',()=>{
    test.style.backgroundColor = "#fff";
    conf.style.backgroundColor = "#fff";
    acti.style.backgroundColor = "#fff";
    reco.style.backgroundColor = "rgba(0, 128, 0, 0.2)";
    deat.style.backgroundColor = "#fff";
    document.querySelector('.conf').style.display = "none";
    document.querySelector('.acti').style.display = "none";
    document.querySelector('.reco').style.display = "block";
    document.querySelector('.deat').style.display = "none";
  });

  deat.addEventListener('click',()=>{
    test.style.backgroundColor = "#fff";
    conf.style.backgroundColor = "#fff";
    acti.style.backgroundColor = "#fff";
    reco.style.backgroundColor = "#fff";
    deat.style.backgroundColor = "rgba(128, 128, 128, 0.2)";
    document.querySelector('.conf').style.display = "none";
    document.querySelector('.acti').style.display = "none";
    document.querySelector('.reco').style.display = "none";
    document.querySelector('.deat').style.display = "block";
  });