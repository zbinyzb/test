<template>
    <div>
      <!-- 面包屑导航 -->
      <BreadMenu :page_name="article_data.title" :lanmu="article_data.lanmu"></BreadMenu>

      <!-- 文章内容 -->
      <el-row :gutter="10">
          <el-col :xs="24" :lg="16">
            <div class="body dweb">
                <div class="header">
                    {{ article_data.title }}
                </div>
            </div>
            <div class="body dweb">
                <div class="dweb">
                    {{ article_data.describe }}
                </div>
            </div>

            <div class="body dweb">
                <!-- 文章内容 -->
                <div class="article-content" v-html="article_data.content">
                </div>
                <div class="clear"></div>
            </div>  
            <div class="body dweb">
                <el-button v-if="article_data.pre_id==0" @click="toOtherPage(article_data.pre_id)" type="info">上一页</el-button>
                <el-button v-else @click="toOtherPage(article_data.pre_id)" type="success">上一页</el-button>
                <el-button v-if="article_data.next_id==0" @click="toOtherPage(article_data.next_id)" type="info">下一页</el-button>
                <el-button v-else @click="toOtherPage(article_data.next_id)" type="success">下一页</el-button>
            </div>              
          </el-col>

          <el-col :xs="24" :lg="8"> 
            <div class="body dweb">
                <el-image
                    style="width: 100px; height: 100px"
                    :src="article_data.cover"
                    :fit="'cover'"></el-image>
            </div>
            <!-- 点赞收藏打赏 -->
            <div class="body dweb like-btn" >
                <el-row>
                    <el-col :span="8">
                        <i v-if="user_article_info.like" class="iconfont icon-dianzan" style="color:#fc5959" @click="toLike()"></i>
                        <i v-else class="iconfont icon-dianzan" @click="toLike()" ></i>
                        </el-col>
                    <el-col :span="8">
                        <i v-if="user_article_info.favor" class="iconfont icon-shoucang" style="color:#ffc815" @click="toFavor()"></i>
                        <i v-else class="iconfont icon-shoucang" @click="toFavor()"></i>
                        </el-col>
                    <el-col :span="8">
                        <i v-if="user_article_info.pay" class="iconfont icon-dashang" style="color:#ffc815"></i>
                        <i v-else class="iconfont icon-dashang" @click="toPay()"></i>
                        </el-col>
                </el-row>
            </div>
            <!-- 评论列表 -->
            <div class="body dweb">
                <div v-for="(item,index) in pinglun_data" :key="index" class="body dweb pinlun-item">
                    {{ item.nickName }} 说：
                    <el-divider></el-divider>
                    {{ item.text }}
                </div>       

                <!-- 分页器 -->
                <div class="dweb" style="margin-top:10px">
                    <el-pagination
                        background
                        layout="prev, pager, next"
                        small
                        :pager-count="5"
                        :total="pinglun_total"
                        :page-size="pinglun_pageSize"
                        @current-change="pingluncurrentChange">
                    </el-pagination>
                </div>        
            </div>
            <!-- 新评论 -->
            <div class="body dweb">
                <el-input
                    type="textarea"
                    :maxlength="120"
                    :rows="2"
                    placeholder="请输入内容"
                    v-model="new_pinglun">
                </el-input> 
                <el-button @click="saveNewPinglun()" type="success">发表评论</el-button>
            </div>
            <div>
                <a id="payLink" href="" target="_blank"></a>
            </div>
          </el-col>
      </el-row>
    </div>
</template>

<script>
import BreadMenu from "../components/BreadMenu"
import axios from 'axios'
import Qs from 'qs'
export default {
    data(){
        return{
            article_id:this.$route.query.id,
            article_data:{},
            user_article_info:{
                // like:false,
                // favor:false,
                // pay:false
            },
            //评论
            new_pinglun:"",
            pinglun_total:100,
            pinglun_pageSize:4,
            pinglun_data:[]

        };
    },
    components:{
        BreadMenu
    },
    watch:{
        $route(to){
            // console.log(to)
            this.article_id = to.query.id
            this.getArticleData(to.query.id)
            this.getUserArticleInfo()
            this.getAllPinglun(1,this.pinglun_pageSize)
        }
    },
    mounted() {
        this.getArticleData(this.article_id)
        this.getAllPinglun(1,this.pinglun_pageSize)
        this.getUserArticleInfo()
    },
    methods: {
        //打赏点击事件
        toPay(){
            axios({
                url:"http://127.0.0.1:9000/api/get-alipay-url/",
                method:"post",
                data:Qs.stringify({
                    token:this.$store.getters.isnotUserlogin,
                    article_id:this.article_id
                }) 
            }).then((res)=>{

                let link = document.getElementById('payLink')
                link.href = res.data.pay_link
                link.click()
                if (confirm('支付完成了嘛？')){
                    console.log('ok')
                }
            })
        },
        //点赞点击事件
        toLike(){
            axios({
                url:"http://127.0.0.1:9000/api/article-like/",
                method:"post",
                data:Qs.stringify({
                    token:this.$store.getters.isnotUserlogin,
                    article_id:this.article_id,
                }),
            }).then((res)=>{
                console.log(res.data)
                if (res.data == "nologin") {
                    alert('尚未登录')
                    return
                }
                if (res.data == 'ok') {
                    this.getUserArticleInfo()
                }
            })
        },
        //收藏点击事件
        toFavor(){
            axios({
                url:"http://127.0.0.1:9000/api/article-favor/",
                method:"post",
                data:Qs.stringify({
                    token:this.$store.getters.isnotUserlogin,
                    article_id:this.article_id,
                }),
            }).then((res)=>{
                console.log(res.data)
                if (res.data == "nologin") {
                    alert('尚未登录')
                    return
                }
                if (res.data == 'ok') {
                    this.getUserArticleInfo()
                }
            })
        },
        //获取互动信息
        getUserArticleInfo(){
            let token = this.$store.getters.isnotUserlogin
            if (token){
                axios({
                url:"http://127.0.0.1:9000/api/user-article-info/",
                method:"post",
                data:Qs.stringify({
                    token:token,
                    article_id:this.article_id,
                }),
            }).then((res)=>{
                console.log(res.data)
                this.user_article_info = res.data
            })
            }
            
        },
        //获取文章评论
        getAllPinglun(page,pageSize){
            axios({
                url:"http://127.0.0.1:9000/api/pinglun/",
                method:"get",
                params:{
                    page,
                    pageSize,
                    article_id:this.article_id,
                }
            }).then((res)=>{
                console.log(res.data)
                this.pinglun_data = res.data.data
                this.pinglun_total = res.data.total
            })
        },
        //发表评论
        saveNewPinglun(){
            if (this.new_pinglun.length == 0){
                alert('内容为空')
                return
            }
            axios({
                url:"http://127.0.0.1:9000/api/pinglun/",
                method:"post",
                data:Qs.stringify({
                    token:this.$store.getters.isnotUserlogin,
                    article_id:this.article_id,
                    text:this.new_pinglun
                })
            }).then((res)=>{
                console.log(res.data)
                if (res.data == 'nologin') {
                    alert('尚未登录')
                    return
                    }
                if (res.data == 'noperm') {
                        alert('权限不足')
                        return
                    }
                if (res.data == 'ok') {
                        this.getAllPinglun(1,this.pinglun_pageSize)
                        this.new_pinglun =''
                    }    
            })
        },
        //评论翻页
        pingluncurrentChange(page){
            // console.log(page)
            this.getAllPinglun(page,this.pinglun_pageSize)
        },
        //跳转文章 上下
        toOtherPage(id){
            if (id==0) {
                alert('没有了')
                return
            }
            this.$router.push({path:"/article",query:{id:id}})
        },
        getArticleData(id){
            // console.log(id)
            axios({
                url:"http://127.0.0.1:9000/api/article-data/",
                method:'get',
                params:{
                    article_id:id
                }
            }).then((res)=>{
                // console.log(res.data)
                this.article_data = res.data
            })
        }
    }

}
</script>

<style scoped>
.body.dweb{
    padding: 10px 10px;
}
.body.dweb .dweb{
    padding: 10px;
    color: #b7b7b7;
    font-size: 12px;
    font-style: italic;
}
.like-btn{
    text-align: center;
    color: #fff;
}
.like-btn i {
    font-size: 30px;
    cursor: pointer;
}
.body.dweb .pinlun-item{
    color: #fff;
    font-size: 18px;
}
</style>