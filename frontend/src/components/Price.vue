<template>
  <div>
      <Index></Index>
      <input ref="stockId" id="stockId" placeholder="請輸入代號">
      <button class="btn btn-primary" name="送出" value="送出" type="submit" @click="addStock">送出</button>
      <button class="btn btn-primary" name="送出" value="送出" type="submit" @click="refreshList">刷新</button>
      <div class="container">
        <table class="row">
            <tr class="row row-cols-3">
                <th class="col-3">代號</th>
                <th class="col-3">價格</th>
                <th class="col-3">單量</th>
                <th class="col-3 ">選項</th>
            </tr>
            <tr v-for="item in msg" :key=item.id class="row row-cols-3">
                <td class="col-3">{{ item.id }} </td>
                <td class="col-3">{{ item.price }}</td>
                <td class="col-3">{{ item.volume }}</td>
                <button class="btn btn-danger col-3" type="submit" @click="removePrice(item.id)"> 刪除 </button>
            </tr>
        </table>
      </div>
  </div>
</template> 
<script>
/* eslint-disable */
import axios from 'axios';
import Index from './Index.vue';
import { ref, reactive, watch } from "vue";
export default {
  setup() {
    const refresh = ref(false)
    const msg = ref('')
    const stockId = ref(null)


    watch(msg, (val,oldVa)=>{
      console.log("val,oldVa", val,oldVa)
    })
    const refreshList = () => {
      refresh.value = true
    }
    
    const getStockPrice = watch( refresh, () => {
        const path = 'http://localhost:8800/realPrice';
        axios.get(path)
          .then((res) => {
            console.log("getStockPrice",res);
            msg.value = res.data;
            console.log("getStockPrice", msg);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            console.error(error);
          });
    })
    const addStock = () => {
        for(let i=0; i < msg.value.length; i++){
          if(msg.value[i]["id"] === parseInt(stockId.value.value)){
            refresh.value = false
            return
          }else{
            refresh.value = true

          }
        }
        const path = 'http://localhost:8800/addPrice';
        watch(refresh, axios.post(path, {id:parseInt(stockId.value.value)})
        .then((res) => {
          console.log(res);
          msg.value = res.data;
        })
        .catch((error) => {
          console.log(error);
          console.error(error);
        }));    
    }
    const removePrice = (stockId) => {
        const path = 'http://localhost:8800/removePrice';
        axios.post(path, { id: stockId } )
          .then((res) => {
            console.log(res);
            msg.value = res.data;
          })
          .catch((error) => {
            console.log(error);
            console.error(error);
          });
    }
    setInterval(() => {
      refresh.value = !refresh.value
    }, 5000)
    return {getStockPrice, addStock, removePrice, msg, refreshList, stockId}
  }
};
</script>

<style>
table tr {
    margin: 15px;
}
</style>