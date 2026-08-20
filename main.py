from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Dict, List

app = FastAPI(
    title="FastAPI Local Dict CRUD API",
    description="مثال بسيط لإدارة البيانات في قاموس محلي (Local Dictionary) باستخدام CRUD operations",
    version="1.0.0"
)

# قاعدة بيانات محليّة مؤقتة على شكل Dictionary
# Key: item_id (int), Value: dict (بيانات العنصر)
items_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "title": "تعلم FastAPI من الصفر",
        "description": "دليل شامل لبناء APIs سريعة ومتطورة",
        "price": 25.5,
        "available": True
    },
    2: {
        "id": 2,
        "title": "أساسيات Python",
        "description": "تعلم أساسيات لغة بايثون بالتفصيل",
        "price": 15.0,
        "available": True
    }
}

# 1. Pydantic Schema لإنشاء عنصر جديد (Create)
class ItemCreate(BaseModel):
    title: str = Field(..., example="كتاب جديد")
    description: Optional[str] = Field(None, example="وصف الكتاب")
    price: float = Field(..., gt=0, example=19.99)
    available: bool = Field(True, example=True)

# 2. Pydantic Schema لتحديث عنصر (Update)
class ItemUpdate(BaseModel):
    title: Optional[str] = Field(None, example="عنوان معدل")
    description: Optional[str] = Field(None, example="وصف معدل")
    price: Optional[float] = Field(None, gt=0, example=29.99)
    available: Optional[bool] = Field(None, example=False)

# 3. Pydantic Schema لإرجاع البيانات في الاستجابة (Response Model)
class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    available: bool


@app.get("/", tags=["الصفحة الرئيسية"])
def read_root():
    """الصفحة الرئيسية للترحيب"""
    return {
        "message": "أهلاً بك في تطبيق FastAPI!",
        "docs_url": "افتح الرابط /docs لتجربة الـ API تفاعلياً"
    }


# ==========================================
# 1. GET Methods (القراءة / الجلب)
# ==========================================

@app.get("/items", response_model=List[ItemResponse], tags=["العناصر (Items)"])
def get_all_items():
    """جلب جميع العناصر الموجودة في الـ Dictionary"""
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=ItemResponse, tags=["العناصر (Items)"])
def get_item_by_id(item_id: int):
    """جلب عنصر معين باستخدام الـ ID الخاص به"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"العنصر رقم {item_id} غير موجود!"
        )
    return items_db[item_id]


# ==========================================
# 2. POST Method (الإضافة / الإنشاء)
# ==========================================

@app.post(
    "/items", 
    response_model=ItemResponse, 
    status_code=status.HTTP_201_CREATED,
    tags=["العناصر (Items)"]
)
def create_item(item: ItemCreate):
    """إضافة عنصر جديد إلى الـ Dictionary"""
    # توليد ID جديد تلقائياً (أكبر ID + 1)
    new_id = max(items_db.keys(), default=0) + 1
    
    new_item_dict = {
        "id": new_id,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "available": item.available
    }
    
    # حفظ العنصر في الـ Dictionary المحلي
    items_db[new_id] = new_item_dict
    
    return new_item_dict


# ==========================================
# 3. PUT Method (التعديل / التحديث)
# ==========================================

@app.put("/items/{item_id}", response_model=ItemResponse, tags=["العناصر (Items)"])
def update_item(item_id: int, item_update: ItemUpdate):
    """تحديث بيانات عنصر موجود مسبقاً"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"العنصر رقم {item_id} غير موجود للتعديل!"
        )
    
    existing_item = items_db[item_id]
    
    # تحديث الحقول المرسلة فقط
    update_data = item_update.model_dump(exclude_unset=True)
    existing_item.update(update_data)
    
    items_db[item_id] = existing_item
    return existing_item


# ==========================================
# 4. DELETE Method (الحذف)
# ==========================================

@app.delete("/items/{item_id}", tags=["العناصر (Items)"])
def delete_item(item_id: int):
    """حذف عنصر من الـ Dictionary"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"العنصر رقم {item_id} غير موجود للحذف!"
        )
    
    deleted_item = items_db.pop(item_id)
    return {
        "message": f"تم حذف العنصر رقم {item_id} بنجاح",
        "deleted_item": deleted_item
    }
