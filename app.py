import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ───────────────────────────────────────────
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🎯",
    layout="wide"
)

# ── Load data ─────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv('data/rfm_segmented.csv')

df = load_data()

# ── Header ────────────────────────────────────────────────
st.title("🎯 Customer Segmentation Dashboard")
st.markdown("**UK Online Retail · RFM Analysis · KMeans Clustering**")
st.divider()

# ── Segment color map ─────────────────────────────────────
COLOR_MAP = {
    'Champions':          '#7c6dfa',
    'Loyal Customers':    '#3dd68c',
    'New / Promising':    '#f5a623',
    'Lost / Hibernating': '#ff5f5f'
}

# ── KPI row ───────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers",  f"{len(df):,}")
col2.metric("Total Revenue",    f"£{df['Monetary'].sum():,.0f}")
col3.metric("Avg Order Value",  f"£{df['Monetary'].mean():,.0f}")
col4.metric("Avg Recency",      f"{df['Recency'].mean():.0f} days")

st.divider()

# ── Segment overview ──────────────────────────────────────
st.subheader("Segment Overview")

seg_summary = df.groupby('Segment').agg(
    Customers     = ('CustomerID', 'count'),
    Avg_Recency   = ('Recency',    'mean'),
    Avg_Frequency = ('Frequency',  'mean'),
    Avg_Monetary  = ('Monetary',   'mean'),
    Total_Revenue = ('Monetary',   'sum')
).round(1).reset_index()

seg_summary['% Revenue'] = (seg_summary['Total_Revenue'] /
                             seg_summary['Total_Revenue'].sum() * 100).round(1)

col1, col2 = st.columns(2)

with col1:
    fig_pie = px.pie(
        seg_summary, values='Customers', names='Segment',
        title='Customer Distribution by Segment',
        color='Segment', color_discrete_map=COLOR_MAP,
        hole=0.4
    )
    fig_pie.update_traces(textposition='outside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    fig_rev = px.bar(
        seg_summary, x='Segment', y='Total_Revenue',
        title='Total Revenue by Segment',
        color='Segment', color_discrete_map=COLOR_MAP,
        text='% Revenue'
    )
    fig_rev.update_traces(texttemplate='%{text}%', textposition='outside')
    fig_rev.update_layout(showlegend=False)
    st.plotly_chart(fig_rev, use_container_width=True)

# ── RFM scatter ───────────────────────────────────────────
st.subheader("RFM Space — Customer Distribution")

col1, col2 = st.columns(2)

with col1:
    fig_scatter = px.scatter(
        df, x='Recency', y='Monetary',
        color='Segment', color_discrete_map=COLOR_MAP,
        title='Recency vs Monetary Value',
        opacity=0.5, size_max=8,
        labels={'Recency': 'Days Since Last Purchase', 'Monetary': 'Total Spend (£)'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    fig_scatter2 = px.scatter(
        df, x='Frequency', y='Monetary',
        color='Segment', color_discrete_map=COLOR_MAP,
        title='Frequency vs Monetary Value',
        opacity=0.5,
        labels={'Frequency': 'Number of Orders', 'Monetary': 'Total Spend (£)'}
    )
    st.plotly_chart(fig_scatter2, use_container_width=True)

# ── Segment detail table ──────────────────────────────────
st.subheader("Segment Profiles")

display_cols = ['Segment','Customers','Avg_Recency','Avg_Frequency','Avg_Monetary','Total_Revenue','% Revenue']
st.dataframe(
    seg_summary[display_cols].rename(columns={
        'Avg_Recency':   'Avg Recency (days)',
        'Avg_Frequency': 'Avg Orders',
        'Avg_Monetary':  'Avg Spend (£)',
        'Total_Revenue': 'Total Revenue (£)',
    }),
    use_container_width=True, hide_index=True
)

# ── Business recommendations ──────────────────────────────
st.subheader("Business Recommendations")

recs = {
    'Champions': ('🏆', 'Reward & retain — VIP program, early access, referral rewards. These are your most valuable customers.'),
    'Loyal Customers': ('💚', 'Upsell & cross-sell — bundle offers, product recommendations. Increase average order value.'),
    'New / Promising':    ('🌱', 'Second-purchase incentive. "Thank you for your recent order — here\'s 10% off your next." Highest growth potential.'),
    'Lost / Hibernating': ('💤', 'Low-cost reactivation only — seasonal email once a quarter. Accept most as churned.'),
}

cols = st.columns(4)
for i, (seg, (icon, action)) in enumerate(recs.items()):
    with cols[i]:
        st.markdown(f"""
        <div style="background:#1c1c21;border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:14px;height:180px">
            <div style="font-size:24px">{icon}</div>
            <div style="font-weight:600;margin:6px 0;color:#f0f0f2">{seg}</div>
            <div style="font-size:12px;color:#9090a0;line-height:1.5">{action}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────
st.divider()
st.caption("Built by Gowri Vinod · IIT Mandi MBA DS&AI · github.com/YOUR_USERNAME/customer-segmentation-ecommerce")