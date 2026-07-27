# ==================================================
# AI Based Email Classification Dashboard
# ==================================================

import streamlit as st
import pandas as pd

from classifier import classify_email


# -----------------------------
# Page Settings
# -----------------------------

st.set_page_config(
    page_title="AI Email Classifier",
    page_icon="📧",
    layout="wide"
)


# -----------------------------
# Load Emails
# -----------------------------

try:

    df = pd.read_csv("emails.csv")

except Exception as e:

    st.error("emails.csv not found")
    st.stop()



# -----------------------------
# Rename Graph API Columns
# -----------------------------

column_mapping = {

    "from": "Sender",
    "subject": "Subject",
    "body": "Body",
    "receivedDateTime": "Date"

}


df.rename(
    columns=column_mapping,
    inplace=True
)



# Create missing columns

required_columns = [
    "Sender",
    "Subject",
    "Body",
    "Date"
]


for col in required_columns:

    if col not in df.columns:

        df[col] = ""



# -----------------------------
# AI Classification
# -----------------------------

category_list = []
confidence_list = []


for index, row in df.iterrows():


    subject = str(row["Subject"])

    body = str(row["Body"])



    try:


        category, confidence = classify_email(

            subject,
            body

        )


    except Exception:


        category = "Unknown"

        confidence = 0



    category_list.append(category)

    confidence_list.append(confidence)



df["Category"] = category_list

df["Confidence"] = confidence_list



# Keep complete data

all_emails_df = df.copy()
# -----------------------------
# Count Categories
# -----------------------------

total_emails = len(all_emails_df)

spam_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Spam"
    ]
)

purchase_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Purchases"
    ]
)

banking_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Banking"
    ]
)

jobs_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Jobs"
    ]
)

exam_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Examinations"
    ]
)

important_count = len(
    all_emails_df[
        all_emails_df["Category"] == "Important"
    ]
)


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title(
    "📧 AI Mail"
)



st.sidebar.button(
    "✏️ Compose"
)



folders = [

    f"📥 Inbox ({total_emails})",

    "⭐ Starred",

    "⏰ Snoozed",

    "📤 Sent",

    "📝 Drafts",

    f"🛒 Purchases ({purchase_count})",

    f"🏦 Banking ({banking_count})",

    f"💼 Jobs ({jobs_count})",

    f"🎓 Examinations ({exam_count})",

    f"❗ Important ({important_count})",

    "📅 Scheduled",

    "📬 All Mail",

    f"🚫 Spam ({spam_count})",

    "🗑 Trash"

]

selected_folder = st.sidebar.radio(

    "Folders",

    folders

)



# -----------------------------
# Title
# -----------------------------

st.title(
    "📧 AI-Based Email Classification Dashboard"
)



# -----------------------------
# Search
# -----------------------------

search = st.text_input(
    "🔍 Search Emails"
)



if search:


    df = df[

        df["Subject"]

        .str.contains(

            search,

            case=False,

            na=False

        )

    ]



# -----------------------------
# Folder Filtering
# -----------------------------

if "🚫 Spam" in selected_folder:

    df = df[
        df["Category"] == "Spam"
    ]


elif "🛒 Purchases" in selected_folder:

    df = df[
        df["Category"] == "Purchases"
    ]


elif "🏦 Banking" in selected_folder:

    df = df[
        df["Category"] == "Banking"
    ]


elif "💼 Jobs" in selected_folder:

    df = df[
        df["Category"] == "Jobs"
    ]


elif "🎓 Examinations" in selected_folder:

    df = df[
        df["Category"] == "Examinations"
    ]


elif "❗ Important" in selected_folder:

    df = df[
        df["Category"] == "Important"
    ]


elif "📥 Inbox" in selected_folder:

    df = df


elif "📬 All Mail" in selected_folder:

    df = df
# -----------------------------
# Summary Cards
# -----------------------------
c1,c2,c3,c4,c5,c6,c7 = st.columns(7)



c1.metric(

    "📧 Total Emails",

    len(all_emails_df)

)


c2.metric(

    "🚫 Spam",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Spam"
        ]
    )

)


c3.metric(

    "🛒 Purchases",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Purchases"
        ]
    )

)


c4.metric(

    "🏦 Banking",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Banking"
        ]
    )

)


c5.metric(

    "💼 Jobs",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Jobs"
        ]
    )

)


c6.metric(

    "🎓 Exams",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Examinations"
        ]
    )

)


c7.metric(

    "❗ Important",

    len(
        all_emails_df[
            all_emails_df["Category"]=="Important"
        ]
    )

)



st.divider()
# -----------------------------
# Category Analytics
# -----------------------------

st.subheader("📊 Email Category Distribution")


category_data = all_emails_df["Category"].value_counts()


st.bar_chart(
    category_data
)



# -----------------------------
# Email List + Preview
# -----------------------------


left,right = st.columns([2,1])



with left:


    st.subheader(
        "📬 Emails"
    )


    if len(df)>0:


        selected_email = st.selectbox(

            "Select Email",

            df["Subject"].tolist()

        )


        display_columns = [

            "Sender",
            "Subject",
            "Category",
            "Confidence",
            "Date"

        ]


        st.dataframe(

            df[display_columns],

            use_container_width=True

        )


    else:


        selected_email = None

        st.warning(
            "No emails found"
        )



# -----------------------------
# Email Preview
# -----------------------------


with right:


    st.subheader(
        "📨 Email Preview"
    )



    if selected_email:


        email = df[

            df["Subject"]==selected_email

        ].iloc[0]



        st.write(

            "👤 Sender:",

            email["Sender"]

        )



        st.write(

            "📌 Subject:",

            email["Subject"]

        )



        st.write(

            "📅 Date:",

            email["Date"]

        )



        st.write(
            "📄 Body:"
        )


        st.text(

            email["Body"]

        )



        st.divider()



        st.subheader(

            "🤖 AI Result"

        )


        st.success(

            "Category: "

            + str(email["Category"])

        )


    confidence = float(email["Confidence"])


if confidence >= 80:

    st.success(
        f"Confidence: {confidence}% (High)"
    )


elif confidence >= 50:

    st.warning(
        f"Confidence: {confidence}% (Medium)"
    )


else:

    st.error(
        f"Confidence: {confidence}% (Low)"
    )
    st.subheader("🤖 AI Model Summary")


st.write(
    """
    The system uses TF-IDF feature extraction
    with Multinomial Naive Bayes classification.

    It automatically categorizes emails into:
    
    - Spam
    - Purchases
    - Banking
    - Jobs
    - Examinations
    - Important

    and provides confidence scores.
    """
)