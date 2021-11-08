<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row :gutter="20">
        <el-col :span="20" :xs="24">
          <el-form
            ref="listQuery"
            :model="listQuery"
            :inline="true"
            label-width="68px"
          >
            <el-form-item label="用户昵称">
              <el-input
                v-model="listQuery.username"
                placeholder="用户昵称"
                clearable
                size="mini"
                style="width: 200px"
                @keyup.enter.native="handleFilter"
              />
            </el-form-item>
            <el-form-item label="笔记标题">
              <el-input
                v-model="listQuery.title"
                placeholder="笔记标题"
                clearable
                size="mini"
                style="width: 200px"
                @keyup.enter.native="handleFilter"
              />
            </el-form-item>
            <el-form-item label="笔记内容">
              <el-input
                v-model="listQuery.content"
                placeholder="笔记内容"
                clearable
                size="mini"
                style="width: 200px"
                @keyup.enter.native="handleFilter"
              />
            </el-form-item>
            <el-form-item>
              <el-button
                v-waves
                type="primary"
                size="mini"
                icon="el-icon-search"
                @click="handleFilter"
              >
                搜索
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-button
                v-waves
                :loading="downloadLoading"
                size="mini"
                type="primary"
                icon="el-icon-download"
                @click="handleDownload"
              >
                导出
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-button
                v-waves
                size="mini"
                type="success"
                icon="el-icon-plus"
                @click="handleCreate"
              >
                添加笔记
              </el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>

      <el-table
        :key="tableKey"
        :data="list"
        v-loading="listLoading"
        aria-setsize
        border
        fit
        highlight-current-row
        style="width: 100%"
      >
        <el-table-column align="center" label="笔记ID" min-width="220">
          <template slot-scope="{ row }">
            <span>{{ row.note_id }}</span>
          </template>
        </el-table-column>

        <el-table-column min-width="280px" align="center" label="标题">
          <template slot-scope="{ row }">
            <span>{{ row.title }}</span>
          </template>
        </el-table-column>

        <el-table-column min-width="100px" align="center" label="点赞数">
          <template slot-scope="{ row }">
            <span>{{ row.collects }}</span>
          </template>
        </el-table-column>

        <el-table-column min-width="150px" align="center" label="用户昵称">
          <template slot-scope="{ row }">
            <span>{{ row.username }}</span>
          </template>
        </el-table-column>

        <el-table-column align="center" min-width="90px" label="评论数">
          <template slot-scope="{ row }">
            <template v-if="row.edit">
              <el-input v-model="row.title" size="small" />
            </template>
            <span v-else>{{ row.comments }}</span>
          </template>
        </el-table-column>

        <el-table-column
          show-overflow-tooltip
          width="600px"
          align="center"
          label="笔记内容"
        >
          <template slot-scope="{ row }">
            <span>{{ row.content }}</span>
          </template>
        </el-table-column>

        <el-table-column align="center" min-width="180px" label="发文时间">
          <template slot-scope="{ row }">
            <span>{{ row.pub_time }}</span>
          </template>
        </el-table-column>

        <el-table-column align="center" min-width="180px" label="更新时间">
          <template slot-scope="{ row }">
            <span>{{ row.update_time }}</span>
          </template>
        </el-table-column>

        <el-table-column label="操作" align="center" fixed="right" min-width="260">
          <template slot-scope="{ row, $index }">
            <el-button
              v-if="row.image_list.length != 0"
              size="mini"
              type="success"
              @click="handleImgList(row)"
            >
              查看图集
            </el-button>
            <el-button type="primary" size="mini" @click="handleUpdate(row)">
              编辑
            </el-button>

            <el-button
              v-if="row.status != 'deleted'"
              size="mini"
              type="danger"
              @click="handleDelete(row, $index)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <pagination
        v-show="total > 0"
        :total="total"
        :page.sync="listQuery.page"
        :limit.sync="listQuery.limit"
        @pagination="getList"
      />

      <el-image-viewer
        v-if="showImgViewer"
        :initial-index="1"
        :on-close="onClose"
        :on-switch="onSwitch"
        :url-list="nowRow.image_list"
      />

      <el-dialog
        :title="textMap[dialogStatus]"
        :visible.sync="dialogFormVisible"
      >
        <el-form
          ref="dataForm"
          :rules="rules"
          :model="temp"
          label-position="left"
          label-width="85px"
          style="width: 600px; margin-left: 35px"
        >
          <el-form-item label="标题" prop="title">
            <el-input v-model="temp.title" />
          </el-form-item>

          <el-form-item label="用户昵称" prop="username">
            <el-input v-model="temp.username" />
          </el-form-item>
          <el-form-item label="点赞数" prop="collects">
            <el-input v-model="temp.collects" />
          </el-form-item>
          <el-form-item label="评论数" prop="comments">
            <el-input v-model="temp.comments" />
          </el-form-item>
          <el-form-item label="笔记内容" prop="content">
            <el-input
              v-model="temp.content"
              :autosize="{ minRows: 4, maxRows: 8 }"
              type="textarea"
              placeholder="Please input"
            />
          </el-form-item>
          <el-form-item label="发布时间" prop="pub_time">
            <el-date-picker
              v-model="temp.pub_time"
              type="datetime"
              placeholder="选择时间"
              value-format="yyyy-MM-dd HH:mm:ss"
            />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false"> 取消</el-button>
          <el-button
            type="primary"
            @click="dialogStatus === 'create' ? createData() : updateData()"
          >
            确认
          </el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import { get_xhs_list } from "@/api/xhs";
import waves from "@/directive/waves"; // waves directive
import { parseTime } from "@/utils";
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  name: "Xhs",
  components: { Pagination },
  directives: { waves },

  data() {
    return {
      tableKey: Math.random(),
      list: null,
      total: 0,
      listLoading: true,
      showImgViewer: false,
      nowRow: "",
      listQuery: {
        page: 1,
        limit: 15,
        title: "",
        username: "",
        content: "",
      },
      cityOptions: ["纽约", "巴黎", "北京"],
      showReviewer: false,
      temp: {},
      dialogFormVisible: false,
      dialogStatus: "",
      textMap: {
        update: "Edit",
        create: "Create",
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        city: [
          { required: true, message: "city is required", trigger: "change" },
        ],

        title: [
          {
            required: true,
            message: "title is required",
            trigger: "change",
          },
        ],
        content: [
          { required: true, message: "content is required", trigger: "change" },
        ],

        collects: [
          {
            required: true,
            message: "collects is required",
            trigger: "change",
          },
        ],
        comments: [
          {
            required: true,
            message: "comments is required",
            trigger: "change",
          },
        ],
        username: [
          {
            required: true,
            message: "username is required",
            trigger: "change",
          },
        ],
        pub_time: [
          {
            required: true,
            message: "pub_time is required",
            trigger: "change",
          },
        ],
      },
      downloadLoading: false,
    };
  },
  created() {
    this.getList();
  },

  methods: {
    // 关闭图片预览
    onClose() {
      this.showImgViewer = false;
    },
    onSwitch(index) {
      // console.log(index)
    },
    getList() {
      this.listLoading = true;
      get_xhs_list(this.listQuery).then((response) => {
        this.list = response.data.items;
        this.total = response.data.total;
        this.listLoading = false;
        setTimeout(() => {}, 1.5 * 1000);
      });
    },

    handleFilter() {
      this.listQuery.page = 1;
      this.getList();
    },

    // 图集
    handleImgList(row) {
      this.showImgViewer = true;
      this.nowRow = row;
    },

    resetTemp() {
      this.temp = {
        city: "成都",
        title: "天安门广场",
        username: "鬼子口音",
        content: "这是一段内容",
        image_list: [],
        collects: 0,
        comments: 0,
        pub_time: this.dayjs().format("YYYY-MM-DD HH:mm:ss"),
        update_time: this.dayjs().format("YYYY-MM-DD HH:mm:ss"),
      };
    },

    handleCreate() {
      this.resetTemp();
      this.dialogStatus = "create";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    createData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          // create_xhs(this.temp).then(() => {
          this.dialogFormVisible = false;
          this.$notify({
            title: "演示环境",
            message: "新增成功",
            type: "warning",
            duration: 2000,
          });
          // });
        }
      });
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row); // copy obj
      this.dialogStatus = "update";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    updateData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp);
          // update_xhs_comment(tempData).then(() => {
          this.dialogFormVisible = false;
          this.$notify({
            title: "Success",
            message: "Update Successfully",
            type: "success",
            duration: 2000,
          });
          // });
        }
      });
    },

    handleDelete(row, index) {
      this.$notify({
        title: "不不不",
        message: "不支持删除操作",
        type: "error",
        duration: 2000,
      });
    },

    handleDownload() {
      this.downloadLoading = true;
      import("@/vendor/Export2Excel").then((excel) => {
        const tHeader = [
          "城市",
          "笔记ID",
          "用户昵称",
          "标题",
          "笔记内容",
          "点赞数",
          "评论数",
          "发布时间",
          "更新时间",
        ];
        const filterVal = [
          "city",
          "note_id",
          "username",
          "title",
          "content",
          "collects",
          "comments",
          "pub_time",
          "update_time",
        ];
        const data = this.formatJson(filterVal);
        var date = new Date();
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: "xhs" + date.toLocaleString("chinese", { hour12: false }),
        });
        this.downloadLoading = false;
      });
    },
    formatJson(filterVal) {
      return this.list.map((v) =>
        filterVal.map((j) => {
          if (j === "timestamp") {
            return parseTime(v[j]);
          } else {
            return v[j];
          }
        })
      );
    },
  },
};
</script>
