<template>
  <div class="Home">
  <Head/>
    <Banner/>
      <div>
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      </div>

    <div >

    </div>
  <Footer ></Footer>
  </div>
</template>

<script>
//导入头部组件
import Head from '../components/Head';
import Footer from '../components/Footer';
import Banner from '../components/Banner';
import axios from "axios";

export default {

  name: 'Home',

  data() {

  },
  created() {
    // axios.get('http://127.0.0.1:8000/home/home/').then((response) => {
    //       console.log(response.data)
    //     }).catch((errors) =>{
    //       console.log(errors)
    // })
  },
    components:{
        Head,Footer,Banner
    },


}


</script>
